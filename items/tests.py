from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Item


class ItemAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.list_url = reverse('item-list-create')

    def authenticate(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'testuser', 'password': 'testpass123'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['access']}"
        )

    def test_items_list_requires_authentication(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_complete_full_crud_flow(self):
        self.authenticate()

        create_response = self.client.post(
            self.list_url,
            {
                'name': 'Mechanical Keyboard',
                'description': '80 percent keyboard',
                'price': '89.99',
                'quantity': 25,
            },
            format='json'
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        item_id = create_response.data['id']

        list_response = self.client.get(self.list_url)
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list_response.data), 1)

        detail_url = reverse('item-detail', kwargs={'pk': item_id})
        detail_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['name'], 'Mechanical Keyboard')

        put_response = self.client.put(
            detail_url,
            {
                'name': 'Mechanical Keyboard Pro',
                'description': 'RGB version',
                'price': '129.99',
                'quantity': 10,
            },
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['name'], 'Mechanical Keyboard Pro')

        patch_response = self.client.patch(
            detail_url,
            {'price': '99.99'},
            format='json'
        )
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['price'], '99.99')

        delete_response = self.client.delete(detail_url)
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)
        self.assertIn('message', delete_response.data)
        self.assertFalse(Item.objects.filter(pk=item_id).exists())
