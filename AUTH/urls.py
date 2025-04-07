from django.urls import path
from .views import *

urlpatterns = [
    path('', auth_home, name="auth_home"),  
    path('email-signup', email_signup, name="email_signup"),  
    path('email-login', email_login, name="email_login"),  
]  