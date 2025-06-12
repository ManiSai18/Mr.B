import random, re, requests, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
from .models import Users, Category, Plan, Person, Expense, Payment
from django.db.models.aggregates import Sum
from datetime import datetime

# Session Decorator (Same as before)
def session_required(view_func):
    def wrapper(request, *args, **kwargs):
        allowed_paths = ['/login/', '/signup/', '/', '/request-password-reset/', '/verify-otp/', '/set-new-password/']
        if request.path in allowed_paths:
            return view_func(request, *args, **kwargs)
        if not request.session.get('user_id'):
            return redirect(f'/login/?next={request.path}')
        return view_func(request, *args, **kwargs)
    return wrapper

# Location Fetching Logic (IP Based)
import requests

def get_location_info():
    try:
        response = requests.get("https://ipapi.co/json/", timeout=3)
        data = response.json()
        return {
            "city": data.get("city", ""),
            "state": data.get("region", ""),
            "zip": data.get("postal", ""),
            "address": data.get("org", ""),
            "location_type": data.get("country_name", "")
        }
    except Exception as e:
        print("Failed to fetch location:", e)
        return {
            "city": "",
            "state": "",
            "zip": "",
            "address": "",
            "location_type": ""
        }

@session_required
def index(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    return render(request, 'budget/index.html')

################# AUTHENTICATION FLOW #################

@session_required
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        contact = request.POST.get('contact')

        if not re.fullmatch(r'^\d{10}$', contact):
            messages.error(request, "Enter valid 10-digit contact.")
            return redirect('signup')
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        encrypted_password = make_password(password)
        Users.objects.create(user_name=name, email=email, password=encrypted_password, contact=int(contact))
        messages.success(request, "Account created!")
        return redirect('login')
    return render(request, 'budget/signup.html')


@session_required
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.user_id
                return redirect('dashboard')
            else:
                messages.error(request, "Incorrect password.")
        except Users.DoesNotExist:
            messages.error(request, "Email not registered.")
    return render(request, 'budget/login.html')


@session_required
def logout_view(request):
    request.session.flush()
    return redirect('login')

@session_required
def request_password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            messages.error(request, "No user found with this email.")
            return redirect('request_password_reset')

        otp = str(random.randint(100000, 999999))
        request.session['reset_email'] = email
        request.session['otp'] = otp

        send_mail(
            'Your OTP Code for Password Reset',
            f'Your OTP is: {otp}',
            'rmani0894@gmail.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, 'OTP sent to your email.')
        return redirect('verify_otp')

    return render(request, 'budget/send_otp.html')

@session_required
def verify_otp_view(request):
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if not session_otp:
            messages.error(request, "Session expired or invalid.")
            return redirect('request_password_reset')

        if otp_input == session_otp:
            return redirect('set_new_password')
        else:
            messages.error(request, 'Invalid OTP.')
            return redirect('verify_otp')

    return render(request, 'budget/verify_otp.html')

@session_required
def set_new_password_view(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        email = request.session.get('reset_email')

        if not email:
            messages.error(request, "Session expired. Please restart.")
            return redirect('request_password_reset')

        try:
            user = Users.objects.get(email=email)
            user.password = make_password(new_password)
            user.save()

            request.session.pop('reset_email', None)
            request.session.pop('otp', None)

            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        except Users.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('request_password_reset')

    return render(request, 'budget/set_new_password.html')


################# DASHBOARD + PLAN FLOW #################

@session_required
def dashboard_view(request):
    user_id = request.session.get('user_id')
    user_name = Users.objects.get(user_id=user_id)
    plans = Plan.objects.filter(user_id=user_id)
    labels, budgets, spent = [], [], []
    for plan in plans:
        total = Expense.objects.filter(plan_id=plan.plan_id).aggregate(Sum('amount_spent'))['amount_spent__sum'] or 0
        labels.append(plan.title)
        budgets.append(plan.initial_budget)
        spent.append(total)
    return render(request, 'budget/dashboard.html', {
        'user_name': user_name, 'plans': plans,
        'chart_labels': labels, 'chart_budget': budgets,
        'chart_spent': spent, 'has_plans': plans.exists()
    })


@session_required
def create_plan_view(request):
    if request.method == 'POST':
        plan = Plan.objects.create(
            user_id=request.session['user_id'],
            title=request.POST['title'],
            initial_budget=request.POST['initial_budget'],
            people_number=request.POST['people_number'],
            from_date=request.POST['from_date'],
            to_date=request.POST['to_date'],
        )

        people_names = request.POST['people_names']
        for name in people_names.split(','):
            name = name.strip()
            if name:
                Person.objects.create(person_name=name, plan=plan)
        return redirect('plan_list')
    return render(request, 'budget/create_plan.html')


@session_required
def plan_list_view(request):
    plans = Plan.objects.filter(user_id=request.session.get('user_id'))
    return render(request, 'budget/plan.html', {'plans': plans})


@session_required
def plan_detail_view(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id, user_id=request.session.get('user_id'))
    if request.method == 'POST':
        plan.title = request.POST['title']
        plan.from_date = request.POST['from_date']
        plan.to_date = request.POST['to_date']
        plan.save()
        return redirect('plan_list')
    return render(request, 'budget/plan_detail.html', {'plan': plan})


@session_required
def view_plan_view(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id, user_id=request.session.get('user_id'))
    people = Person.objects.filter(plan_id=plan_id)
    expenses = Expense.objects.filter(plan_id=plan_id).order_by('date', 'time')
    return render(request, 'budget/view_plan.html', {
        'plan': plan, 'people': people, 'expenses': expenses
    })


@session_required
def all_persons_view(request):
    user_id = request.session.get('user_id')
    persons = Person.objects.filter(plan__user_id=user_id)
    return render(request, 'budget/all_persons.html', {'persons': persons})

@session_required
def all_payments_view(request):
    payments = Payment.objects.all()
    return render(request, 'budget/all_payments.html', {'payments': payments})


################# EXPENSE MODULE #################

@session_required
def add_expense_view(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    people = Person.objects.filter(plan=plan)
    payment_methods = Payment.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        current_time = datetime.now().time()
        person_id = request.POST.get('person')
        person = Person.objects.get(person_id=person_id)
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        time = current_time  # Capture current time
        expense_title = request.POST.get('description')
        payment_method = Payment.objects.get(payment_method_id=request.POST.get('payment_method'))
        category = Category.objects.get(category_id=request.POST.get('category'))

        # Fetch location from form (from JS)
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip")
        address = request.POST.get("address")
        location_type = request.POST.get("location_type")

        Expense.objects.create(
            plan=plan, person=person, amount_spent=amount,
            expense_title=expense_title, date=date, time=time,
            payment_method=payment_method, category=category,
            city=city, state=state, zip=zip_code,
            address=address, location_type=location_type
        )
        return redirect('view_plan', plan.plan_id)

    return render(request, 'budget/add_expense.html', {
        'plan': plan, 'people': people,
        'payment_methods': payment_methods, 'categories': categories
    })


@session_required
def edit_expense_view(request, expense_id):

    expense = get_object_or_404(Expense, expense_id=expense_id)
    plan = expense.plan
    people = Person.objects.filter(plan=plan)
    payment_methods = Payment.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        expense.person = Person.objects.get(person_id=request.POST.get('person'))
        expense.amount_spent = request.POST.get('amount')
        expense.date = request.POST.get('date')
        expense.expense_title = request.POST.get('description')
        expense.payment_method = Payment.objects.get(payment_method_id=request.POST.get('payment_method'))
        expense.category = Category.objects.get(category_id=request.POST.get('category'))
        expense.time = datetime.now().time()
        expense.city = request.POST.get("city")
        expense.state = request.POST.get("state")
        expense.zip = request.POST.get("zip")
        expense.address = request.POST.get("address")
        expense.location_type = request.POST.get("location_type")

        expense.save()
        return redirect('view_plan', plan.plan_id)

    return render(request, 'budget/edit_expense.html', {
        'expense': expense, 'plan': plan, 'people': people,
        'payment_methods': payment_methods, 'categories': categories
    })

@session_required
def delete_expense_view(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    plan_id = expense.plan_id
    expense.delete()
    return redirect('view_plan', plan_id=plan_id)


@session_required
def expense_distribution_view(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    people = Person.objects.filter(plan=plan)
    expenses = Expense.objects.filter(plan=plan)

    total_spent = expenses.aggregate(Sum('amount_spent'))['amount_spent__sum'] or 0
    total_people = people.count()
    expected_share = total_spent / total_people if total_people else 0

    distribution = {p.person_name: expenses.filter(person=p).aggregate(Sum('amount_spent'))['amount_spent__sum'] or 0 for p in people}
    share_diff = {name: round(amount - expected_share, 2) for name, amount in distribution.items()}
    top_spender = max(distribution.items(), key=lambda x: x[1])[0] if distribution else None

    context = {
        'plan': plan, 'expenses': expenses, 'total_spent': total_spent,
        'total_people': total_people, 'expected_share': expected_share,
        'distribution': distribution, 'share_diff': share_diff, 'top_spender': top_spender,
        'names': list(distribution.keys()), 'values': list(distribution.values())
    }
    return render(request, 'budget/expense_distribution.html', context)

