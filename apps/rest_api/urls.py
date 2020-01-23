from django.urls import path, include
from apps.rest_api import views
from rest_framework import routers

# Way 1 (using router)
router = routers.DefaultRouter()
# Routers automatically determine how the URLs for an application should be mapped
# to the logic that deals with handling incoming requests.
# DefaultRouter: https://www.django-rest-framework.org/api-guide/routers/

router.register('categories', views.CategoryView)
router.register('posts', views.PostView, base_name='post')
# base_name is used to specify the initial part of the view name pattern.

urlpatterns = [
	path('', include(router.urls)),

	# Way 2 (manually)
	path('comments/', views.CommentListView.as_view(), name='comment-list'),
	path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail')
	# as_view() function returns a callable view that takes a request and returns a response.
	# name defines which name is provided to the URL pattern defined.
]
