from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from apps.account import forms, views

urlpatterns = [
	path('login/', LoginView.as_view(authentication_form=forms.AuthenticationForm), name='login'),
	path('sign_up/', views.SignUp.as_view(), name='sign-up'),
	path('', include('django.contrib.auth.urls')),
	path('', TemplateView.as_view(template_name='account.html'), name='account'),
]
