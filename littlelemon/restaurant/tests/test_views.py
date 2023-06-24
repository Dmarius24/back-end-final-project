from django.test import TestCase
from unittest import TestCase

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menuitem1 = MenuItem.objects.create(title="Pizza", price=10.99, inventory=10)
        self.menuitem2 = MenuItem.objects.create(title="Burger", price=8.99, inventory=14)
        self.menuitem3 = MenuItem.objects.create(title="Salad", price=7.99, inventory=20)

    def test_getall(self):
        url = reverse("menu-list")
        response = self.client.get(url)
        menuitems = MenuItem.objects.all()
        serializer = MenuItemSerializer(menuitems, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)