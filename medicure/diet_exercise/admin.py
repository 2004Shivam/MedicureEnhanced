from django.contrib import admin
from .models import UserHealthProfile, DietPlan, ExercisePlan, VitaminDeficiency, ExerciseCategory

admin.site.register(VitaminDeficiency)
admin.site.register(ExerciseCategory)

@admin.register(UserHealthProfile)
class UserHealthProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'bmi_category')
    
    def bmi_category(self, obj):
        # Allow checking BMI directly from list view
        bmi = obj.weight / ((obj.height / 100) ** 2)
        return f"{bmi:.1f}"

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created', 'daily_calories', 'goal')

@admin.register(ExercisePlan)
class ExercisePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created', 'goal', 'total_duration')
