from django import forms
from .models import Ingredient,BakeryItem, Inventory

class ingredientform(forms.Form):
    class Meta:
        model=Ingredient
        fields=[
            "id",
            "name",
        ]

class bakeryitemform(forms.Form):
    class Meta:
        model=BakeryItem
        fields=[
            "name",
            "costprice",
            "sellingprice",
        ]

class inventoryform(forms.Form):
    class Meta:
        model=Inventory
        fields=[

            "name",
            "quantity",
            "ingredient",
        ]

