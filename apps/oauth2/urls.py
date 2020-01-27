from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from apps.oauth2 import views

urlpatterns = [
	path('', views.index, name='index'),

	path('', include('social_django.urls', namespace='social')),
	# URL namespaces allow you to uniquely reverse named URL patterns. It is a
	# good practice for third-party apps to always use namespaced URLs. The namespace
	# parameter takes on special meaning when you deploy multiple instances of the
	# same App in the same project.
	path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')
	# LogoutView is a class provided by Django framework that logs a user out.
	# Attribute next_page means the URL to redirect after the logout (by default
	# it is used the settings.LOGOUT_REDIRECT_URL value).
]
