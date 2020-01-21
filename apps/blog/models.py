from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=30)

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='posts')

# created_on and last_modified are Django DateTimeFields. These store a datetime
# object containing the date and time when the post was created and modified
# respectively. We have configured them to be an automatic process.
# auto_now_add=True sets the date and time when the instance is created.
# auto_now=True sets the date and time when the instance is saved.

# ManytoManyField field links the Post and Category models and allows us to create
# a relationship between the two tables. The first argument is the model with which
# the relationship is. The second argument allows us to access the relationship
# from a Category object, even though we have not added a field there. By adding
# a related_name of posts, we can access category.posts to give us a list of posts
# with that category.

class Comment(models.Model):
	author = models.CharField(max_length=70)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

# The ForeignKey field is similar to the ManyToManyField but instead defines a many
# to one relationship. The reasoning behind this is that many comments can be assigned
# to one post. The first argument is the other model in the relationship. The second
# argument tells Django what to do when a post is deleted.
