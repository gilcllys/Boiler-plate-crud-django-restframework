from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from core import serializer, custom_serializer, behavior
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.GenericAPIView):
    permission_classes = ()
    serializer_class = custom_serializer.RegisterCustomSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = behavior.RegisterBehavior(data=data_serializer).run()
        return response


class LoginView(TokenObtainPairView):

    def get(self, request):
        data = request.data
        serializer = custom_serializer.LoginCustomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = behavior.LoginBehavior(data=data_serializer).run()
        return response


class LogoutView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = custom_serializer.RegisterCustomSerializer

    def post(self, request):
        data = request.data
        serializer = custom_serializer.LogoutCustomSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = behavior.LogoutBehavior(data=data_serializer).run()
        return response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserSerializer
    queryset = User.objects.all()
