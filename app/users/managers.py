import logging
from typing import Optional

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError("The email must be set")

        if not password:
            logging.warning("Password empty, faulting to default value")
            kwargs['password'] = '123'

        kwargs['role'] = kwargs.get('role', 4)
        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.role = kwargs['role']

        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs['role'] = 0

        return self.create_user(email, password, **kwargs)

    def soft_delete_user(self, uid: Optional[str] = None, email: Optional[str] = None):

        if uid is not None:
            user = self.model.objects.get(id=uid)
        else:
            user = self.model.objects.get(email=email)

        if not user:
            raise self.model.DoesNotExist(
                f"User with {'uid=' + uid if uid else 'email=' + email} not found")

        user.is_active = False
        user.save()

        user.refresh_from_db()

        return user
