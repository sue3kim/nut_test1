from django.db import models

class Food(models.Model):
    CATEGORY_CHOICES = (
        ('low_cal', 'Low Calorie'),
        ('carbs', 'Carbohydrates'),
        ('protein', 'Protein'),
        ('fat', 'Fat')
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    calories = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
class Consumption(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField()  # in grams
    date = models.DateField(auto_now_add=True)