from rest_framework import serializers
from .models import Ingredient,BakeryItem, IngredientPercentage,Inventory

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'



class IngredientPercentageSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientPercentage
        fields = ('ingredient', 'percentage')

class BakeryItemSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientPercentageSerializer(many=True)

    class Meta:
        model = BakeryItem
        fields = '__all__'


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = Inventory
        fields = '__all__'