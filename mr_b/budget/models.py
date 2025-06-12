from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'contact']

    def __str__(self):
        return self.user_name



class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    initial_budget = models.BigIntegerField()
    people_number = models.IntegerField()
    title = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.title


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.person_name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Payment(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_method_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.payment_method_name


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
    expense_title = models.CharField(max_length=255, null=True)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)
    amount_spent = models.BigIntegerField(null=True)
    bill = models.BinaryField(null=True, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)
    location_type = models.CharField(max_length=50, null=True)
    balance_amount = models.BigIntegerField(null=True)

    payment_method = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL, related_name='expenses')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.expense_title} - ${self.amount_spent}"
