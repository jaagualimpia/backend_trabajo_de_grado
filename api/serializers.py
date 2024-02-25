from api.models import User, Diagnosis
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Diagnosis
        fields = "__all__"

class DiagnosisPostSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Diagnosis
        fields = ['patient_date_of_birth', 'patient_name', 'image_url', 'user']