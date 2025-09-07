from rest_framework import serializers
from app.users.models import User, UserRoles


class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'role', 'email', 'created_at',
                  'updated_at', 'password', 'is_active')

    def get_role(self, obj: User):
        return UserRoles.get_str_from_num(obj.role.numerator)
