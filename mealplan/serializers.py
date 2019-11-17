from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from mealplan.models import Day, MealPlan, GroceryList, GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = [
            'id',
            'name',
            'checked',
        ]


class GroceryListSerializer(WritableNestedModelSerializer):
    items = GroceryItemSerializer(many=True, required=False)

    class Meta:
        model = GroceryList
        fields = [
            'id',
            'items'
        ]


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = [
            'id',
            'choice',
            'link',
            'restaurant',
            'meal',
            'source',
        ]


class MealPlanSerializer(WritableNestedModelSerializer):
    days = DaySerializer(many=True, required=False)
    grocery_list = GroceryListSerializer(required=False)

    class Meta:
        model = MealPlan
        fields = [
            'id',
            'days',
            'grocery_list'
        ]
