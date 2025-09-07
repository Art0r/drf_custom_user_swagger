from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.users.models import User
from app.users.permissions import IsEmployeeOrItself, IsEmployeeOrHigher
from app.users.serializers.retrieve import RetrieveUserSerializer


class RetrieveUserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsEmployeeOrHigher)

    def retrieve(self, request, *args, **kwargs):
        return super(RetrieveUserViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(RetrieveUserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(RetrieveUserViewSet, self).destroy(request, *args, **kwargs)
