from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ACTIVITY_CHOICES = [
        (1.2, 'Sedentary'),
        (1.375, 'Lightly Active'),
        (1.55, 'Moderately Active'),
        (1.725, 'Very Active'),
        (1.9, 'Extra Active'),
    ]
    GOAL_CHOICES = [
        ('loss', 'Weight Loss'),
        ('maintain', 'Maintenance'),
        ('gain', 'Weight Gain'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age = models.IntegerField(default=25)
    height = models.FloatField(default=170.0) # in cm
    weight = models.FloatField(default=70.0)  # in kg
    activity_level = models.FloatField(choices=ACTIVITY_CHOICES, default=1.2)
    goal_type = models.CharField(max_length=10, choices=GOAL_CHOICES, default='maintain')
    
    # Calculated Targets
    calorie_goal = models.IntegerField(default=2000)
    protein_goal_pct = models.IntegerField(default=25)
    carbs_goal_pct = models.IntegerField(default=50)
    fats_goal_pct = models.IntegerField(default=25)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.0)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} consumed {self.food_consumed.name}"
