from account.enum import NotificationType, UserRole

class AppHelpers:

    @staticmethod
    def get_user_role_name(role):
        return UserRole[role].value
    
    @staticmethod
    def get_user_notification_type_name(types):
        return NotificationType(types).name