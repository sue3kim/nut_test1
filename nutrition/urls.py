from django.urls import path
from .views import NutrientRecommendation

urlpatterns = [
    path('recommend/', NutrientRecommendation.as_view(), name='nutrient_recommendation'),
]