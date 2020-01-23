from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from apps.rest_api import views, models, serializers

class PostViewTest(APITestCase):
	# APITestCase it is similar to Django's TestCase.
	# https://docs.djangoproject.com/en/3.0/topics/testing/tools/#testcase

	client = APIClient()
	# APIClient it is similar to Django's Client.
	# Useful to make HTTP Request using HTTP methods like GET, POST, etc.

	def setUp(self):
		# This method is called before each test method is executed.

		animals_category = models.Category.objects.create(name='Animals')
		education_category = models.Category.objects.create(name='Education')

		# Create Post 1
		models.Post.objects.create(
			title='My first post',
			body='This is a post related to animals.'
		).categories.set([animals_category])

		# Create Post 2
		models.Post.objects.create(
			title='My second post',
			body='This is a post related to education.'
		).categories.set([education_category])

		# Create Post 3
		models.Post.objects.create(
			title='My third post',
			body='This is a post related to animals and education.'
		).categories.set([animals_category, education_category])

	def test_get_all_posts(self):
		"""
		This test ensures that all posts has been added in the setUp method
		and they exist when making a GET request to '/posts' endpoint.
		"""
		expected = models.Post.objects.all()
		serializer = serializers.PostSerializer(expected, many=True)

		response = self.client.get(reverse('post-list'))

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_post_new_post(self):
		"""
		This test ensures that it is possible to create a new post making a POST
		request to '/posts' endpoint.
		"""
		category_id = models.Category.objects.all().first().id
		post_data = {
			'title': 'My fourth post',
			'body': 'This is a post related to animals.',
			'categories': [category_id]
		}

		response = self.client.post(reverse('post-list'), data=post_data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		post = models.Post.objects.get(title='My fourth post')
		serializer = serializers.PostSerializer(post)

		# Checking if the first dictionary is a subset of the second dictionary
		self.assertTrue(post_data.items() <= serializer.data.items())

	def test_get_single_post(self):
		"""
		This test ensures that posts are accessible through their id making a GET
		request to '/posts/<int:pk>' endpoint.
		"""
		post_id=3
		expected = models.Post.objects.get(pk=post_id)
		serializer = serializers.PostSerializer(expected)

		response = self.client.get(reverse('post-detail', args={post_id}))

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_single_post(self):
		"""
		This test ensures that posts can be deleted through their id making a
		DELETE request to '/posts/<int:pk>' endpoint.
		"""
		post_id=3

		self.assertTrue(models.Post.objects.filter(pk=post_id).exists())

		response = self.client.delete(reverse('post-detail', args={post_id}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

		response = self.client.get(reverse('post-detail', args={post_id}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

		self.assertFalse(models.Post.objects.filter(pk=post_id).exists())
