from rest_framework.viewsets import ModelViewSet

from mealplan.models import MealPlan, GroceryList
from mealplan.serializers import MealPlanSerializer, GroceryListSerializer


class MealPlanViewSet(ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer


class GroceryListViewSet(ModelViewSet):
    queryset = GroceryList.objects.all()
    serializer_class = GroceryListSerializer
