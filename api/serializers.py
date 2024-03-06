from api.models import User, Diagnosis
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ["id", "diagnosis_result", "diagnosis_date", "patient_date_of_birth", "patient_name", "image_url"]
 
 
class DiagnosisPostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Diagnosis
        fields = ['id', 'patient_date_of_birth', 'patient_name', 'image_url', 'user']

class DiagnosisDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Diagnosis
        fields = ["id", "diagnosis_result", "diagnosis_date", "patient_date_of_birth", "patient_name", "image_url", "user", "username"]