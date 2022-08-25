from django.db import models

class UserRole(models.IntegerChoices):
    PARENT = 1
    STUDENT = 2
    SUPER_ADMIN = 3
    COLLEGE = 4


class UserStatus(models.IntegerChoices):
    NOT_APPROVED = 0
    APPROVED = 1
    ON_HOLD = 2


class NotificationType(models.IntegerChoices):
    STUDENT_APPROVAL = 1
    FOOD_MENU = 2


class MealType(models.IntegerChoices):
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3


class StatusType(models.IntegerChoices):
    DRAFT = 1
    PUBLISHED = 2



class MealStatus(models.IntegerChoices):
    UNAPPROVED = 0
    ACCEPTED = 1
    TAKEN = 2