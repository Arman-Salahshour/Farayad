from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin



class UserManager(BaseUserManager):

    def create_user(self,username,email,password,**extra_fields):

        if not email:
            raise ValueError("You must set an email")
        if not username:
            raise ValueError("You must set an username")
        if not password:
            raise ValueError("You must set an password")


        email = self.normalize_email(email)
        user=self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,username,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)

        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Admin must have is_admin=True.')
        
        self.create_user(username,email,password,**extra_fields)


