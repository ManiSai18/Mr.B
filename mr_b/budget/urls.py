from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('create-plan/', views.create_plan_view, name='create_plan'),
    path('plans/', views.plan_list_view, name='plan_list'),
    path('plan/<int:plan_id>/edit/', views.plan_detail_view, name='plan_detail'),
    path('plan/<int:plan_id>/', views.view_plan_view, name='view_plan'),
    
    path('all-persons/', views.all_persons_view, name='all_persons'),
    path('all-payments/', views.all_payments_view, name='all_payments'),

    path('plan/<int:plan_id>/add-expense/', views.add_expense_view, name='add_expense'),
    path('expense/<int:expense_id>/edit/', views.edit_expense_view, name='edit_expense'),
    path('expense/<int:expense_id>/delete/', views.delete_expense_view, name='delete_expense'),

    path('plan/<int:plan_id>/distribution/', views.expense_distribution_view, name='expense_distribution'),

    path('request-password-reset/', views.request_password_reset, name='request_password_reset'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('set-new-password/', views.set_new_password_view, name='set_new_password'),
]
