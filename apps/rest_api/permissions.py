from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
	# BasePermission allows you to implement custom permissions, overriding one
	# or both methods that it provides:
	# - has_permission(self, request, view)
	# - has_object_permission(self, request, view, obj)
	#
	# https://www.django-rest-framework.org/api-guide/permissions/

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			# Permissions for read-only request
			return True
		else:
			# Permissions for write request
			return False
	# If you need to check if a request is a read operation or a write operation,
	# you should check the request method against the constant SAFE_METHODS, which
	# is a tuple containing 'GET', 'OPTIONS' and 'HEAD'.
