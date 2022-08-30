from rest_framework import serializers
from rest_framework.authtoken.models import Token
from E_college.helper import AppHelpers

from account.models import StudentMeal, User, UserNotification
from account.enum import MealStatus, NotificationType, UserRole, UserStatus



class RequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    role = serializers.ChoiceField(choices=[UserRole.STUDENT.name,UserRole.PARENT.name])

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'status','role','token')

    def get_token(self,user):
        token,is_created = Token.objects.get_or_create(user=user)
        return AppHelpers.get_user_token(token.key)

    def get_status(self,user):
        return  AppHelpers.get_status_name(user.status)

    def get_role(self,user):
        return  AppHelpers.get_user_role_name(user.role)

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


