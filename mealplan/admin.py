from django.contrib import admin

from mealplan.models import MealPlan, Day, GroceryList, GroceryItem

admin.site.register(MealPlan)
admin.site.register(Day)
admin.site.register(GroceryList)
admin.site.register(GroceryItem)
