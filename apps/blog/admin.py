from django.contrib import admin
from apps.blog.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
	pass

class PostAdmin(admin.ModelAdmin):
	pass

# Defined empty classes PostAdmin and CategoryAdmin. For the purposes of this tutorial,
# you do not need to add any attributes or methods to these classes. They are used
# to customize what is shown on the admin pages.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

# These last two lines are the most important. These register the models with the
# admin classes.
