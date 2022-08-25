from django.urls import path
from account.views import LoginAPIView, StudentMenuTakenViewSet, StudentMenuViewSet,UserNotificationViewSet,StatusUpdateAPI

urlpatterns = [
    path('login/', LoginAPIView.as_view({'post':'post'}),name='login_view' ),
    path('notification/',UserNotificationViewSet.as_view({'get':'get'}), name='user_notification'),
    path('students/<int:student_id>/',StatusUpdateAPI.as_view({'patch':'patch'}),name='statusupdate'),
    path('menu/<int:meal_id>/approved',StudentMenuViewSet.as_view({'put':'put'})),
    path('menu/taken',StudentMenuTakenViewSet.as_view({'patch':'patch'})),
]