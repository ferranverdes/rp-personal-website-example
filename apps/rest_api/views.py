from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.rest_api import models, serializers

# Way 1 (using Viewsets - ModelViewSet)
class CategoryView(viewsets.ModelViewSet):
	# ModelViewSet includes implementations for various actions (list, retrieve,
	# create, update, partial_update and destroy)
	queryset = models.Category.objects.all()
	serializer_class = serializers.CategorySerializer
	# As a queryset, we need to specify how django can query the database to get all entries.
	# As a serializer_class, we need to indicate which class is able to serialize our instances.

# Way 1.2 (using Viewsets - ViewSet)
# serializer: https://www.django-rest-framework.org/api-guide/serializers/
# (serializer.is_valid(), serializer.save(), serializer.delete(), serializer.data,
# serializer.error, serializer(context={}), etc) have a look at link above.
class PostView(viewsets.ViewSet):
	# The ViewSet class inherits from APIView. The ViewSet class does not provide
	# any implementations of actions. In order to use a ViewSet class you will
	# override the class and define the action implementations explicitly.
	serializer_class = serializers.PostSerializer

	def list(self, request):
		"""HTTP GET /posts/"""
		queryset = models.Post.objects.all()
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		"""HTTP POST /posts/"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""HTTP GET /posts/<int:pk>"""
		queryset = models.Post.objects.all()
		post = get_object_or_404(queryset, pk=pk)
		serializer = self.serializer_class(post)
		return Response(serializer.data)

	def update(self, request, pk=None):
		"""HTTP PUT /posts/<int:pk>"""
		queryset = models.Post.objects.all()
		post = get_object_or_404(queryset, pk=pk)
		serializer = self.serializer_class(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk=None):
		"""HTTP DELETE /posts/<int:pk>"""
		# if models.Post.objects.filter(pk=pk).exists():
		#	post = models.Post.objects.get(pk=pk)
		#	post.delete()
		#	return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(status=status.HTTP_404_NOT_FOUND)

# Way 2 (using APIView)
class CommentListView(APIView):
	# Using the APIView, the incoming request is dispatched to an appropriate handler
	# method such as .get(), .post(), put() or delete().
	serializer_class = serializers.CommentSerializer

	def get(self, request):
		"""HTTP GET /comments/"""
		queryset = models.Comment.objects.all()
		serializer_context = { 'request': request }
		serializer = self.serializer_class(queryset, many=True, context=serializer_context)
		return Response(serializer.data)

	def post(self, request):
		"""HTTP POST /comments/"""
		serializer_context = { 'request': request }
		serializer = self.serializer_class(data=request.data, context=serializer_context)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
	serializer_class = serializers.CommentSerializer

	def get(self, request, pk=None):
		"""HTTP GET /comments/<int:pk>"""
		queryset = models.Comment.objects.all()
		comment = get_object_or_404(queryset, pk=pk)
		serializer_context = { 'request': request }
		serializer = self.serializer_class(comment, context=serializer_context)
		return Response(serializer.data)

	def delete(self, request, pk=None):
		"""HTTP DELETE /comments/<int:pk>"""
		if models.Comment.objects.filter(pk=pk).exists():
			comment = models.Comment.objects.get(pk=pk)
			comment.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(status=status.HTTP_404_NOT_FOUND)
