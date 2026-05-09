from django.urls import path
from .views import ItemListCreateView, ItemDetailView, AdminOnlyView, MeView, SendTestEmailView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('admin-panel/', AdminOnlyView.as_view(), name='admin-panel'),
    path('me/', MeView.as_view(), name='me'),
    path('send-email/', SendTestEmailView.as_view(), name='send-email'),
]