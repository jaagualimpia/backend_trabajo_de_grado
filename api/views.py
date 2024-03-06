from django.shortcuts import render
from api.models import User, Diagnosis
from rest_framework import permissions, viewsets
from api.serializers import DiagnosisDetailSerializer, UserSerializer, DiagnosisSerializer, DiagnosisPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status 
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from django.core import serializers

# Create your views here.

jwt_authentication = JWTAuthentication()

class DiagnosisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows diagnosis to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Diagnosis.objects.all().order_by('-diagnosis_date')
    serializer_class = DiagnosisSerializer

    def list(self, request):
        user, token = jwt_authentication.authenticate(request)
        pk = user.id
        queryset = Diagnosis.objects.filter(user_id=pk).order_by('-diagnosis_date')
        
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]

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
        
class DiagnosisList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user, token = jwt_authentication.authenticate(request)

            request.data["user"] = user.id        
            diagnosis = DiagnosisPostSerializer(data=request.data)
            
            if diagnosis.is_valid():

                diagnosis.save()
                return Response(diagnosis.data, status=status.HTTP_201_CREATED)
            else:
                return Response(diagnosis.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DiagnosisDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            user, token = jwt_authentication.authenticate(request)
            diagnosis = Diagnosis.objects.get(pk=pk, user=user.id)
            serializer = DiagnosisDetailSerializer(instance=diagnosis)
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)