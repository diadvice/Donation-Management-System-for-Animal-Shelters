from django.shortcuts import render
from .models import *

# Create your views here.

def get_available_bonuses(user):
    """Retrieve all bonuses associated with the user's plan."""
    if user.plan:
        return user.plan.bonuses.all()
    return []


def select_bonus(user, bonus_id):
    """Mark the user's selected bonus."""
    try:
        selected_bonus = Bonus.objects.get(id=bonus_id)
        user.selected_bonus = selected_bonus
        user.save()
        return f"Вы выбрали бонус: {selected_bonus.description} от компании {selected_bonus.company_name}. Переходите по {selected_bonus.link} , чтобы получить бонус."
    except Bonus.DoesNotExist:
        return "Выбранный бонус не существует."


def start_plan_date(user,donation):
    """Starts the timer of the plan_expiration_date after first donation."""
    if user.current_total_donation_amount==0:
        user.plan_start_date=donation.donation_date 

def check_donation_goal(user):
    """Check if the user has reached their donation goal."""
    if user.donations >= user.donation_goal:
        return True
    return False


def update_donation_received(user, donation_amount):
    """Update the user's donation total and check if the goal is reached."""
    user.donations += donation_amount
    user.save()

    if check_donation_goal(user):
        plan = user.plan
        bonuses = plan.get_bonuses_list()
        return f"Поздравляю! Вы набрали нужную сумму и достигли своей месячной цели. Выберите любой бонус по вашему уровню: {', '.join(bonuses)}"
    return f"Спасибо за Вашу помощь приюту! Ваша текущая накопленная сумма {user.donations}/{user.donation_goal}."


def select_bonus(user, selected_bonus):
    """Mark the user's selected bonus and store it in the database."""
    user.selected_bonus = selected_bonus
    user.save()
    return f"Круто! Ваш выбранный бонус: {selected_bonus}"


def set_user_plan(user, plan_id):
    """Set the plan user choosed."""
    user.plan=plan_id


def view_bonuses(plan):
    """Allows user to view bonuses within each plan"""

    if plan:
        bonuses = plan.bonuses.all()  # Fetch all bonuses associated with the plan
        result = []

        # Show the bonuses regardless of the user's donation progress
        for bonus in bonuses:
            result.append({
                'name': bonus.name,
                'description': bonus.description,
                'company': bonus.company_name,
                'link': 'Link will be unlocked when you complete the donation goal',  # Do not reveal the link
            })
        return result
    return []

   
def unlock_bonus_link_for_user(user):
    """Unlock the link for bonuses after the user reaches the donation goal."""
    if user.current_donations >= user.donation_goal:
        return user.plan.bonuses.all()  # Return all bonuses, including the link
    return "You haven't reached your donation goal yet."

def renew_plan():
    """Sets all plan and donation goal to empty once the goal was completed or the date expired"""




#generate individual promocodes
#id is connected to the promocode
#send to email or to tg bot




# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt
# def handle_plan_selection(request, user_id, plan):
#     if request.method == 'POST':
#         user, _ = User.objects.get_or_create(user_id=user_id)
#         user.selected_plan = plan
#         user.save()
#         return JsonResponse({'status': 'Plan selected'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# @csrf_exempt
# def handle_city_selection(request, user_id, city):
#     if request.method == 'POST':
#         user = User.objects.get(user_id=user_id)
#         user.city = city
#         user.save()
#         return JsonResponse({'status': 'City selected'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# @csrf_exempt
# def handle_receipt_upload(request, user_id):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         receipt_file_id = data.get('receipt_file_id')
#         user = User.objects.get(user_id=user_id)
#         user.receipt_uploaded = receipt_file_id
#         user.save()
#         return JsonResponse({'status': 'Receipt uploaded'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# def get_bonuses(request, user_id):
#     bonuses = Bonus.objects.filter(is_claimed=False)
#     bonus_list = [{'description': bonus.description} for bonus in bonuses]
#     return JsonResponse({'bonuses': bonus_list})
