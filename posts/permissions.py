from rest_framework import permissions


class BasePermission(object):
    """
    A base class from which all permission classses should inherit.
    """

    def has_permission(self, request, view):
        """
        Return 'True' if permission is granted, 'False' otherside.
        """
        return True
    
    def has_object_permission(self, request, view, obj):
        """
        Return 'True' if permission is granted, 'False' otherside
        """
        return True
    

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user