from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return False


# class SuperuserPermission(BasePermission):
    # def has_permission(self, request, view):
        #return bool(request.user and request.user.is_superuser)
        # return request.user.is_superuser
    # def has_object_permission(self, request, view, obj):
    #     if request.user.is_superuser():
    #         return True
    #     else:
    #         return False
