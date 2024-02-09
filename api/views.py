from django.shortcuts import render
from api.models import User, Diagnosis
from rest_framework import permissions, viewsets
from api.serializers import UserSerializer, DiagnosisSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status 
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class DiagnosisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows diagnosis to be viewed or edited.
    """
    queryset = Diagnosis.objects.all().order_by('-diagnosis_date')
    serializer_class = DiagnosisSerializer
    permission_classes = [permissions.AllowAny]

class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]

    #TODO post method in SignUpView with authentication
    def post(self, request):
        user = UserSerializer(data=request.data)

        if user.is_valid():
            password = user.validated_data["password"]

            user.validated_data["password"] = make_password(user.validated_data["password"])
            print("Validando que si sea", check_password(password, user.validated_data["password"]))

            user.save()

            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthenticationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data
        print(user)
        
        user_in_db = User.objects.get(username=user["username"])

        if not check_password(user["password"], user_in_db.password):
            return Response(data={"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"token": "1234"}, status=status.HTTP_200_OK)