from rest_framework import serializers
from apps.rest_api import models

# Serializers: https://www.django-rest-framework.org/api-guide/serializers/#serializers

# Way 1 (creating a serializer manually)
class CategorySerializer(serializers.Serializer):
	# Serializers allow complex data such as querysets and model instances to be
	# converted to JSON, XML or other content types. Serializers also provide
	# deserialization, allowing parsed data to be converted back into native Python
	# datatypes, after first validating the incoming data.
	id = serializers.ReadOnlyField()
	url = serializers.HyperlinkedIdentityField(view_name='category-detail', read_only=True)
	name = serializers.CharField(max_length=30)

	def create(self, validated_data):
		category = models.Category.objects.create(**validated_data)
		return category
		# ** collects all the keyword arguments in a dictionary.

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name')
		instance.save()
		return instance

# Way 2 (using predefined serializers)
class PostSerializer(serializers.ModelSerializer):
	# ModelSerializer class is the same as a regular Serializer class, except that
	# it automatically generates a set of fields for you, based on the model, it
	# automatically generates validators for the serializer and it also includes
	# simple default implementations of .create() and .update().
	class Meta:
		model = models.Post
		fields = '__all__'
		# Meta is an inner class that contains any information that can be considered
		# as metadata like model, fields, exclude, widgets.

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Comment
		fields = ('id', 'url', 'author', 'body', 'created_on', 'post')
