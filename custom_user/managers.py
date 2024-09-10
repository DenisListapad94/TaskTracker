from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone, password, **kwargs):
        user = self.model(phone=phone, **kwargs)
        user.password = make_password(password)
        user.save()
        return user
        
    def create_user(self, phone, password):
        return self._create_user(phone, password)
        
    def create_superuser(self, phone, password):
        kwargs = {
            'is_superuser': True,
            'is_staff': True,
        }
        return self._create_user(phone, password, **kwargs)
