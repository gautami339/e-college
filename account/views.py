from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from account.enum import UserRole, UserStatus
from account.models import StudentMeal, User, UserNotification, UserRelation
from account.serializer import StatusupdateSerializer, StudentMenuTakenSerializer, StudentMenuUpdateSerializer, StudentSerializer, UserNotificationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from E_college.helper import AppHelpers



class LoginAPIView(ModelViewSet):
    
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer
    
    def post(self, request):

        serializer = self.serializer_class(data = request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({'message':'User Not found'},status=status.HTTP_400_BAD_REQUEST)

        try:
            role = AppHelpers.get_user_role_name(request.data['role'])
            user = User.objects.get(username=request.data['username'],role=role)
        except User.DoesNotExist:
            return Response({'message':'User Not found'},status=status.HTTP_400_BAD_REQUEST)

        Token.objects.get_or_create(user=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        


class UserNotificationViewSet(ModelViewSet):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer

    def get(self,request):
        serializer = self.serializer_class(self.queryset,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class StatusUpdateAPI(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusupdateSerializer


    def patch(self,request,student_id):
        try:
            user_relation = UserRelation.objects.get(parent=request.user,student_id=student_id)
        except UserRelation.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(user_relation.student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentMenuViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = StudentMenuUpdateSerializer


    def put(self,request,meal_id):
        try:
            student_meal =  StudentMeal.objects.get(user=request.user,meal_id=meal_id)
        except StudentMeal.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(student_meal,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class StudentMenuTakenViewSet(ModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentMenuTakenSerializer

    def patch(self,request,token):
        try:
            student_meal =  StudentMeal.objects.get(user=request.user)
        except StudentMeal.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(student_meal,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



