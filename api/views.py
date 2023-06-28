from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingredient,BakeryItem, Inventory
from .serializers import IngredientSerializer,BakeryItemSerializer, InventorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class BakeryItemViewSet(viewsets.ModelViewSet):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class BakeryItemDetailViewSet(viewsets.ModelViewSet):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class CustomerOrderHistoryViewSet(viewsets.ModelViewSet):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer