from django.db import models
from django import forms
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    # Add other fields as needed

    def __str__(self):
        return self.name
    
class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientPercentage')
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other fields as needed

    def __str__(self):
        return self.name
    

class IngredientPercentage(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields as needed

    def __str__(self):
        return f"{self.ingredient} - {self.percentage}%"



class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.ingredient}: {self.quantity}"


