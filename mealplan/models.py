from django.db import models


class MealPlan(models.Model):
    user = models.ForeignKey('profiles.User', on_delete=models.CASCADE, related_name='meal_plans')
    start_date = models.DateField()


class Day(models.Model):
    DINE_IN = 'dine in'
    DINE_OUT = 'dine out'
    CHOICES = (
        (DINE_IN, 'Dine In'),
        (DINE_OUT, 'Dine Out')
    )

    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='days')
    choice = models.CharField(max_length=10, choices=CHOICES)
    link = models.URLField(null=True, blank=True)
    restaurant = models.CharField(max_length=256, null=True, blank=True)
    meal = models.CharField(max_length=256, null=True, blank=True)
    source = models.TextField(null=True, blank=True)


class GroceryList(models.Model):
    meal_plan = models.OneToOneField(MealPlan, on_delete=models.CASCADE, related_name='grocery_list')


class GroceryItem(models.Model):
    grocery_list = models.ForeignKey(GroceryList, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=256)
    checked = models.BooleanField(default=False)
