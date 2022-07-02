from cmath import log
from time import time
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from pkg_resources import Requirement
from django_quill.fields import QuillField

class UserManager(BaseUserManager):

    def create_user(self,username,email,password,**extra_fields):

        if not email:
            raise ValueError("You must set an email")
        if not username:
            raise ValueError("You must set an username")
        if not password:
            raise ValueError("You must set an password")

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
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



def user_directory_path(instance,filename):
    return f'users/{filename}'

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to= user_directory_path, blank=True, null=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects=UserManager()

    def __str__(self):
        return self.username


class GeneralCategory(models.Model):
    name= models.CharField(max_length=100)

    class Meta:
        verbose_name = 'general category'
        verbose_name_plural = 'general categories'

    def __str__(self):
        return self.name   


class Category(models.Model):
    name= models.CharField(max_length=100)
    parent_category= models.ForeignKey(GeneralCategory, on_delete=models.CASCADE, )
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
def course_directory_path(instance,filename):
    return f'courses/{filename}'

class Course(models.Model):
    header= models.CharField(max_length=120, unique=True, blank=False, null=False)
    description= QuillField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE, )
    author= models.ForeignKey(User, on_delete=models.CASCADE, )
    time= models.IntegerField(default=0)
    price=models.FloatField(default=0.0)
    logo=models.ImageField(upload_to= course_directory_path, blank=True, null=True)
    requirements= models.TextField(blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.header}:{self.author}'


class Season(models.Model):
    header = models.CharField(max_length=120, blank=False, null=False)
    description= QuillField()
    video=models.CharField(max_length=400, blank=True, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('course', 'header'),)
        
    def __str__(self):
        return f'{self.course.header}:{self.header}'


class Comment(models.Model):
    text=models.TextField(blank=False, null=False)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course.header}:{self.user}'

def news_directory_path(instance,filename):
    return f'news/{filename}'

class News(models.Model):
    header= models.CharField(max_length=120, unique=True, blank=False, null=False)
    description= QuillField()
    author= models.ForeignKey(User, on_delete=models.CASCADE, )
    logo=models.ImageField(upload_to= news_directory_path, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.header}:{self.author}'


class Payment(models.Model):
    purchaser= models.ForeignKey(User, on_delete=models.CASCADE)
    course= models.ForeignKey(Course, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('purchaser', 'course'),)

    def __str__(self):
        return f'{self.course.header}:{self.purchaser}'