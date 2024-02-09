from api.models import User, Diagnosis
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['diagnosis_result', 'diagnosis_date', 'patient_date_of_birth', 'patient_name', 'image_url']