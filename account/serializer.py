
from email.policy import default
from turtle import update
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from E_college.helper import AppHelpers

from account.models import StudentMeal, User, UserNotification
from account.enum import MealStatus, NotificationType, UserRole, UserStatus



class StudentSerializer(serializers.Serializer):
    username = serializers.CharField()
    role = serializers.ChoiceField(choices=[UserRole.STUDENT.name,UserRole.PARENT.name])



class UserNotificationSerializer(serializers.ModelSerializer):
    types = serializers.SerializerMethodField()

    class Meta:
        model = UserNotification
        fields = ('user_id', 'message', 'types')
    
    def get_types(self,obj):
        return AppHelpers.get_user_notification_type_name(obj.types)


class StatusupdateSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(write_only=True,default=UserStatus.APPROVED.value)
    class Meta:
        model = User
        fields = ('status',)



class StudentMenuUpdateSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(write_only=True, default=MealStatus.ACCEPTED.value)

    class Meta: 
        model = StudentMeal
        fields = ('status',)

class StudentMenuTakenSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(write_only=True, default=MealStatus.TAKEN.value)

    class Meta: 
        model = StudentMeal
        fields = ('status',)
    

