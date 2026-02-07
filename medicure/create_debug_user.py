import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicure.settings')
django.setup()

from django.contrib.auth import get_user_model
from diet_exercise.models import UserHealthProfile, DietPlan, ExercisePlan

User = get_user_model()
username = 'testuser_debug'
email = 'test_debug@example.com'
password = 'TestPass123'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_user(username=username, email=email, password=password)
    user.is_verified = True
    user.save()
    print(f"Created user: {username} (Verified)")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_verified = True
    user.save()
    print(f"Updated user: {username} (Verified)")

# Ensure profile
profile, created = UserHealthProfile.objects.get_or_create(
    user=user,
    defaults={
        'age': 30,
        'gender': 'male',
        'height': 180,
        'weight': 80,
        'goal': 'weight_loss',
        'activity_level': 'moderate'
    }
)
print(f"Profile: {profile}")

# Realistic Mock Data
breakfast_data = [
    {
        'title': 'Oatmeal with Blueberries',
        'calories': 350,
        'nutrition': {'protein': 12, 'carbohydrates': 60, 'fat': 8},
        'ingredients': ['Oats', 'Blueberries', 'Almonds', 'Honey'],
        'instructions': {'steps': [{'step': 'Cook oats in water.'}, {'step': 'Add berries and nuts.'}]}
    }
]
lunch_data = [
    {
        'title': 'Grilled Chicken Salad',
        'calories': 450,
        'nutrition': {'protein': 35, 'carbohydrates': 15, 'fat': 22},
        'ingredients': ['Chicken breast', 'Spinach', 'Tomato', 'Cucumber', 'Olive oil'],
        'instructions': {'steps': [{'step': 'Grill chicken.'}, {'step': 'Mix vegetables.'}, {'step': 'Toss with oil.'}]}
    }
]
dinner_data = [
    {
        'title': 'Baked Salmon with Asparagus',
        'calories': 550,
        'nutrition': {'protein': 40, 'carbohydrates': 10, 'fat': 30},
        'ingredients': ['Salmon fillet', 'Asparagus', 'Lemon', 'Garlic'],
        'instructions': {'steps': [{'step': 'Preheat oven to 400F.'}, {'step': 'Bake salmon for 15 mins.'}]}
    }
]
snacks_data = [
    {
        'title': 'Greek Yogurt',
        'calories': 150,
        'nutrition': {'protein': 15, 'carbohydrates': 10, 'fat': 4},
        'ingredients': ['Greek yogurt', 'Honey'],
        'instructions': {'steps': [{'step': 'Mix and eat.'}]}
    }
]

# Ensure plans (clean old ones first)
DietPlan.objects.filter(user=user).delete()
ExercisePlan.objects.filter(user=user).delete()

DietPlan.objects.create(
    user=user,
    bmi_category='normal',
    goal='weight_loss',
    daily_calories=2000,
    breakfast=json.dumps(breakfast_data),
    lunch=json.dumps(lunch_data),
    dinner=json.dumps(dinner_data),
    snacks=json.dumps(snacks_data)
)
# We don't need to manually populate meal_data here as PlanResultsView handles it from strings.

# Exercises Data
exercises_data = {
    'warm_up': {
        'activities': ['Light jogging', 'Dynamic stretching'],
        'duration': '10'
    },
    'main_workout': [
        {'name': 'Pushups', 'sets': 3, 'reps': 15, 'rest': 60, 'instructions': ['Keep back straight.', 'Lower chest to floor.']},
        {'name': 'Bodyweight Squats', 'sets': 3, 'reps': 20, 'rest': 60, 'instructions': ['Feet shoulder width.', 'Keep weight on heels.']}
    ],
    'cool_down': {
        'activities': ['Static stretching', 'Deep breathing'],
        'duration': '5'
    }
}

ExercisePlan.objects.create(
    user=user,
    bmi_category='normal',
    goal='weight_loss',
    exercises=exercises_data,
    total_duration=45
)
print("Plans ensured.")
