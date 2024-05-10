from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=50)
    recipe_ingredients=models.CharField(max_length=200)
    instructions=models.TextField()
    cuisine=models.CharField(max_length=50)
    meal_type=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe_name

class Review(models.Model):
    recipe_name=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.DecimalField(max_digits=2,decimal_places=1,validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username