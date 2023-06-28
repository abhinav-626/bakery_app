from django.contrib import admin
from django.urls import path,include
from .views import IngredientViewSet, BakeryItemViewSet, BakeryItemDetailViewSet, InventoryViewSet, CustomerOrderViewSet, CustomerOrderHistoryViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'ingredient',IngredientViewSet)
router.register(r'bakery',BakeryItemViewSet)
router.register(r'bakeryitem',BakeryItemDetailViewSet)
router.register(r'inventory',InventoryViewSet)
router.register(r'customer',CustomerOrderViewSet)
router.register(r'customerorder',CustomerOrderHistoryViewSet)


urlpatterns = router.urls

 