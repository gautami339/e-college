from django.db import models
from django.contrib.auth.models import AbstractUser

from account.enum import MealStatus, MealType, NotificationType, StatusType, UserRole, UserStatus


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=50,null=True)
    status = models.IntegerField(choices=UserStatus.choices)
    role = models.IntegerField(choices=UserRole.choices)


class UserRelation(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_student')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_parent')



class UserNotification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    types = models.IntegerField(choices=NotificationType.choices)


class Items(BaseModel):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=150)


class Meal(BaseModel):
    type = models.IntegerField(choices=MealType.choices)
    status = models.IntegerField(choices=StatusType.choices)
    date = models.DateField()


class MealItem(BaseModel):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    item =  models.ForeignKey(Items, on_delete=models.CASCADE)



class StudentMeal(BaseModel):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=MealStatus.choices)