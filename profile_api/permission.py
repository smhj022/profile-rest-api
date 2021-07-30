from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile or not"""

        # safe method means HTTP GET request
        if request.method in permissions.SAFE_METHODS:
            return True

        # if user is trying to update their own id it will return True 
        # else it will return False
        return obj.id == request.user.id

    