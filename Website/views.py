from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Food, Consume, Profile
from django.http import JsonResponse
from datetime import date, timedelta
from django.db.models import Sum

@login_required
def index(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Get the date from query params or default to today
    selected_date_str = request.GET.get('date')
    if selected_date_str:
        try:
            today = date.fromisoformat(selected_date_str)
        except ValueError:
            today = date.today()
    else:
        today = date.today()

    if request.method == "POST":
        # Handle custom food entry
        if 'add_custom_food' in request.POST:
            name = request.POST.get('name')
            carbs = request.POST.get('carbs')
            protein = request.POST.get('protein')
            fats = request.POST.get('fats')
            calories = request.POST.get('calories')
            Food.objects.create(name=name, carbs=carbs, protein=protein, fats=fats, calories=calories)
            messages.success(request, f"Custom food '{name}' added to database!")
            return redirect('index')

        # Handle consumption logging
        food_id = request.POST.get('food_consumed')
        quantity = float(request.POST.get('quantity', 1.0))
        try:
            food = Food.objects.get(id=food_id)
            consume = Consume(user=request.user, food_consumed=food, quantity=quantity)
            consume.save()
            messages.success(request, f"Added {quantity}x {food.name} to your log.")
        except Food.DoesNotExist:
            messages.error(request, "Food item not found.")
        return redirect('index')

    foods = Food.objects.all().order_by('name')
    consumed_food = Consume.objects.filter(user=request.user, date=today).order_by('-id')
    
    # Calculate totals
    total_calories = 0
    total_carbs = 0
    total_protein = 0
    total_fats = 0
    
    for item in consumed_food:
        total_calories += item.food_consumed.calories * item.quantity
        total_carbs += item.food_consumed.carbs * item.quantity
        total_protein += item.food_consumed.protein * item.quantity
        total_fats += item.food_consumed.fats * item.quantity

    # Goal targets (grams)
    # 1g Carb = 4 cal, 1g Protein = 4 cal, 1g Fat = 9 cal
    protein_goal_grams = (profile.calorie_goal * (profile.protein_goal_pct / 100)) / 4
    carbs_goal_grams = (profile.calorie_goal * (profile.carbs_goal_pct / 100)) / 4
    fats_goal_grams = (profile.calorie_goal * (profile.fats_goal_pct / 100)) / 9

    # Calculate weekly progress (last 7 days)
    weekly_labels = []
    weekly_intake = []
    for i in range(6, -1, -1):
        day = date.today() - timedelta(days=i)
        day_logs = Consume.objects.filter(user=request.user, date=day)
        day_total = sum(item.food_consumed.calories * item.quantity for item in day_logs)
        weekly_labels.append(day.strftime('%a')) # 'Mon', 'Tue' etc.
        weekly_intake.append(round(day_total, 1))

    context = {
        'foods': foods,
        'consumed_food': consumed_food,
        'profile': profile,
        'total_calories': round(total_calories, 1),
        'total_carbs': round(total_carbs, 1),
        'total_protein': round(total_protein, 1),
        'total_fats': round(total_fats, 1),
        'protein_goal_grams': round(protein_goal_grams, 1),
        'carbs_goal_grams': round(carbs_goal_grams, 1),
        'fats_goal_grams': round(fats_goal_grams, 1),
        'cal_percent': (total_calories / profile.calorie_goal * 100) if profile.calorie_goal > 0 else 0,
        'selected_date': today.isoformat(),
        'is_today': today == date.today(),
        'weekly_labels': weekly_labels,
        'weekly_intake': weekly_intake
    }
    return render(request, 'index.html', context)

@login_required
def delete_consume(request, id):
    try:
        consumed_food = Consume.objects.get(id=id, user=request.user)
        consumed_food.delete()
        messages.success(request, "Item removed.")
    except Consume.DoesNotExist:
        messages.error(request, "Item not found.")
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def update_goal(request):
    if request.method == 'POST':
        goal = request.POST.get('calorie_goal')
        p_pct = request.POST.get('protein_goal_pct')
        c_pct = request.POST.get('carbs_goal_pct')
        f_pct = request.POST.get('fats_goal_pct')
        
        # Simple validation
        if int(p_pct) + int(c_pct) + int(f_pct) != 100:
            messages.error(request, "Macros must add up to 100%")
            return redirect('index')

        profile = request.user.profile
        profile.calorie_goal = goal
        profile.protein_goal_pct = p_pct
        profile.carbs_goal_pct = c_pct
        profile.fats_goal_pct = f_pct
        profile.save()
        messages.success(request, "Goals updated.")
    return redirect('index')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update profile fields
        profile.gender = request.POST.get('gender', 'M')
        profile.age = int(request.POST.get('age', 25))
        profile.height = float(request.POST.get('height', 170))
        profile.weight = float(request.POST.get('weight', 70))
        profile.activity_level = float(request.POST.get('activity_level', 1.2))
        profile.goal_type = request.POST.get('goal_type', 'maintain')
        
        # Calculate BMR using Mifflin-St Jeor equation
        if profile.gender == 'M':
            bmr = (10 * profile.weight) + (6.25 * profile.height) - (5 * profile.age) + 5
        else:
            bmr = (10 * profile.weight) + (6.25 * profile.height) - (5 * profile.age) - 161
        
        # Calculate TDEE
        tdee = bmr * profile.activity_level
        
        # Adjust for goal
        if profile.goal_type == 'loss':
            profile.calorie_goal = int(tdee - 500)  # 500 cal deficit
            profile.protein_goal_pct = 35
            profile.carbs_goal_pct = 35
            profile.fats_goal_pct = 30
        elif profile.goal_type == 'gain':
            profile.calorie_goal = int(tdee + 300)  # 300 cal surplus
            profile.protein_goal_pct = 30
            profile.carbs_goal_pct = 45
            profile.fats_goal_pct = 25
        else:  # maintain
            profile.calorie_goal = int(tdee)
            profile.protein_goal_pct = 25
            profile.carbs_goal_pct = 50
            profile.fats_goal_pct = 25
        
        profile.save()
        messages.success(request, "Profile updated successfully! Your nutrition targets have been recalculated.")
        return redirect('profile')
    
    # Calculate current BMR and TDEE for display
    if profile.gender == 'M':
        bmr = (10 * profile.weight) + (6.25 * profile.height) - (5 * profile.age) + 5
    else:
        bmr = (10 * profile.weight) + (6.25 * profile.height) - (5 * profile.age) - 161
    
    tdee = bmr * profile.activity_level
    bmi = profile.weight / ((profile.height / 100) ** 2)
    
    context = {
        'profile': profile,
        'bmr': round(bmr, 0),
        'tdee': round(tdee, 0),
        'bmi': round(bmi, 1),
    }
    return render(request, 'profile.html', context)
