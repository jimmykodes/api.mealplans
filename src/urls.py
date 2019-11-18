from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from mealplan.viewsets import MealPlanViewSet, GroceryListViewSet

router = routers.DefaultRouter()
router.register('mealplans', MealPlanViewSet)
router.register('grocery_lists', GroceryListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
