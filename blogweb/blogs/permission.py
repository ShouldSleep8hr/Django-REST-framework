from rest_framework import permissions

class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # Allow POST requests (i.e., creation) only if the user is authenticated
        return request.user.is_authenticated
    
class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the blog.
        return obj.user == request.user
