from django.contrib import admin
from apps.rest_api import models

# Way 1: using a decorator
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	pass

# Way 2: using the register function
class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Comment, CommentAdmin)

# The ModelAdmin class is the representation of a model in the admin interface.
# It has several options for dealing with customizing the interface, for example
# showing only a subset of available fields, modifying their order, or grouping
# them into rows. Have a look at: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
