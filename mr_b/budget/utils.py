import random
from django.core.mail import send_mail

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'Mr. Budget - Password Reset OTP'
    message = f'Your OTP for password reset is: {otp}'
    from_email = 'rmani0894@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
