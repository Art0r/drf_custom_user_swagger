from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.users.models import User
from app.users.permissions import IsManagerOrHigher
from app.users.serializers.list import ListUserSerializer


class ListUserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.prefetch_related('pets').all()
    serializer_class = ListUserSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (
        permissions.IsAuthenticated,
        IsManagerOrHigher
    )
    pagination_class = LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.order_by('-is_active', 'email')
        return super(ListUserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ListUserViewSet, self).create(request, *args, **kwargs)
