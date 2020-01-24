from django.urls import path, include
from apps.rest_api import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

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
	path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
	# as_view() function returns a callable view that takes a request and returns a response.
	# name defines which name is provided to the URL pattern defined.

	path('token-auth/', obtain_auth_token, name='token_auth')
	# We need to make a POST request to this url in order to get a valid token:
	# POST /api/token-auth/ HTTP/1.1
	#
	# {
	# 	"username": "admin",
	# 	"password": "admin"
	# }
	#
	# Providing valid credentials, we will receive a response like this:
	#
	# {
	# 	"token": "c7b51d053bec85b793b3add2830ae486f132ed4c"
	# }
	#
	# Once we have received the token, we can start requesting everything that is
	# under token authentication using the following Auhtentication header in every
	# HTTP request:
	# 'Authorization: Token c7b51d053bec85b793b3add2830ae486f132ed4c'
]
