from account.enum import NotificationType, UserRole, UserStatus

class AppHelpers:

    @staticmethod
    def get_user_role_value(role):
        return UserRole[role].value

    @staticmethod
    def get_user_role_name(role):
        return UserRole(role).name

    @staticmethod
    def get_status_name(role):
        return UserStatus(role).name

    @staticmethod
    def get_user_notification_type_name(types):
        return NotificationType(types).name

    @staticmethod
    def get_user_token(token):
        return 'Token {}'.format(token)
