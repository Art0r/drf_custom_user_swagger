from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from app.users.models import UserRoles


class IsManagerOrHigher(BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.role <= int(UserRoles.manager.value)


class IsEmployeeOrHigher(BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.role <= int(UserRoles.employee.value)


class IsEmployeeOrItself(BasePermission):
    def has_permission(self, request: Request, view):
        return (request.user.role <= int(UserRoles.employee.value)) or (view.kwargs.get('pk') == str(request.user.id))
