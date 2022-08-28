from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from account.enum import MealStatus, MealType, NotificationType, StatusType, UserRole, UserStatus


class UserManager(BaseUserManager):


    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', UserStatus.APPROVED.value )
        extra_fields.setdefault('role', UserRole.SUPER_ADMIN.value)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        super_user = self.model(username=username, **extra_fields)
        super_user.set_password(password)
        super_user.save()
        return super_user


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=150,null=True)
    status = models.IntegerField(choices=UserStatus.choices)
    role = models.IntegerField(choices=UserRole.choices)

    objects = UserManager()


class UserRelation(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_student')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_parent')



class UserNotification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    types = models.IntegerField(choices=NotificationType.choices)


class Item(BaseModel):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=150)


class Meal(BaseModel):
    type = models.IntegerField(choices=MealType.choices)
    status = models.IntegerField(choices=StatusType.choices)
    date = models.DateField()


class MealItem(BaseModel):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)



class StudentMeal(BaseModel):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=MealStatus.choices)