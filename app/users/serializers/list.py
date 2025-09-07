from rest_framework import serializers
from app.users.models import User, UserRoles


class ListUserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'role', 'email', 'created_at',
                  'updated_at', 'password', 'is_active')

    def get_role(self, obj: User):
        return obj.role
