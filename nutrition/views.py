from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer
import random

class NutrientRecommendation(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        total_calories = request.data.get('total_calories')
        total_carbs = request.data.get('total_carbs')
        total_protein = request.data.get('total_protein')
        total_fat = request.data.get('total_fat')
        
        recommended_calories = request.data.get('recommended_calories')
        recommended_carbs = request.data.get('recommended_carbs')
        recommended_protein = request.data.get('recommended_protein')
        recommended_fat = request.data.get('recommended_fat')
        
        if None in [total_calories, total_carbs, total_protein, total_fat, recommended_calories, recommended_carbs, recommended_protein, recommended_fat]:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        

        response_data = {}

        if total_calories >= recommended_calories:
            response_data['message'] = 'Reduce your food intake. Here are some low-calorie food recommendations.'
            low_cal_foods = Food.objects.filter(category='low_cal')
            response_data['recommendations'] = FoodSerializer(random.sample(list(low_cal_foods), 3), many=True).data
        else:
            nutrient_deficit = {
                'carbs': recommended_carbs - total_carbs,
                'protein': recommended_protein - total_protein,
                'fat': recommended_fat - total_fat
            }
            most_deficit = max(nutrient_deficit, key=nutrient_deficit.get)
            response_data['message'] = f'You need more {most_deficit}. Here are some recommendations.'
            nutrient_foods = Food.objects.filter(category=most_deficit)
            response_data['recommendations'] = FoodSerializer(random.sample(list(nutrient_foods), 3), many=True).data
        
        return Response(response_data, status=status.HTTP_200_OK)