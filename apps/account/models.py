from django.db import models
from django.contrib.auth import models as auth_models

class User(auth_models.AbstractUser):
	# Changing the default value to False and the name shown in the admin interface
	# to 'User activated'.
	is_active = models.BooleanField(default=False, verbose_name='User activated')
