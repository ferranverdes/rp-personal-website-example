from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from apps.account.forms import AuthenticationForm

urlpatterns = [
	path('login/', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
	path('', include('django.contrib.auth.urls')),
	path('', TemplateView.as_view(template_name='profile.html'), name='account'),
]
