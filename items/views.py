from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings

from .models import Item
from .serializers import ItemSerializer
from .permissions import IsAdminOrStaff, IsAuthenticatedReadOnly


class ItemListCreateView(APIView):
    """
    GET  /api/items/  → any authenticated user
    POST /api/items/  → admin/staff only
    """
    permission_classes = [IsAuthenticatedReadOnly]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET              /api/items/<id>/  → any authenticated user
    PUT/PATCH/DELETE /api/items/<id>/  → admin/staff only
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        item_name = instance.name
        instance.delete()
        return Response(
            {"message": f"Item '{item_name}' has been deleted successfully."},
            status=status.HTTP_200_OK
        )


class AdminOnlyView(APIView):
    """
    GET /api/admin-panel/
    A dedicated endpoint that only admin/staff can access.
    Regular authenticated users get 403.
    """
    permission_classes = [IsAdminOrStaff]

    def get(self, request):
        return Response({
            "message": "Welcome to the admin panel.",
            "user": request.user.username,
            "is_staff": request.user.is_staff,
            "is_superuser": request.user.is_superuser,
        }, status=status.HTTP_200_OK)


class MeView(APIView):
    """
    GET /api/me/
    Returns the current user's info and role.
    Any authenticated user can access this.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "is_staff": request.user.is_staff,
            "is_superuser": request.user.is_superuser,
            "role": "admin" if (request.user.is_staff or request.user.is_superuser) else "user",
        })

class SendTestEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        recipient = request.data.get('to')
        if not recipient:
            return Response({"error": "No recipient provided."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            send_mail(
                subject='Test Email from Django',
                message='This is a test email sent from the Django Items API.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
            return Response({"message": f"Email sent to {recipient}."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)