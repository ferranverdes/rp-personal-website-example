from django.urls import path
from apps.portfolio import views

urlpatterns = [
	path('', views.project_list, name='project_list'),
	path('<int:pk>', views.project_detail, name='project_detail')
]

# The pk value in the URL is the same pk passed to the view function.
# <int:pk> notation just tells Django that the value passed in the URL is an
# integer, and its variable name is pk.
