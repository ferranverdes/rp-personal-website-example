from django.urls import path
from apps.blog import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('posts/<int:pk>', views.post_detail, name='post_detail'),
	path('categories/<category>', views.category_post_list, name='category_post_list')
]
