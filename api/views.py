from django.shortcuts import render
from api.models import User, Diagnosis
from rest_framework import permissions, viewsets
from api.serializers import UserSerializer, DiagnosisSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status 


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

        print(request.data)

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

class AuthenticationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(data={"token": "1234"}, status=status.HTTP_200_OK)