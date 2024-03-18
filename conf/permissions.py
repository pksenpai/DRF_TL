'''
BasePermission: A class that you must inherit to create custom permissions
SAFE_METHODS: A set of methods that are only for read and safe to use
==========================================================================
SAFE_METHODS Methods(HTTP method):
    --> 'GET', 'OPTIONS', 'HEAD'
    
BasePermission Methods(class method):
    --> .has_object_permission(self, request, view, obj)
        call after that entered view
    
    --> .has_permission(self, request, view)
        call before that enter view
    
'''
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    # There is a default message error, but you can override that too!
    message = "permission denied, you are not the owner!" # like this...
    
    
    def has_permission(self, request, view): # call befor enter to the view
        return request.user.is_authenticated and request.user # check user is authenticated?
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: # GET, OPTIONS, HEAD
            return True
        return obj.author == request.user # check user is the object owner? 
        
