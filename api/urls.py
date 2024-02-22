from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

router = routers.DefaultRouter()
router.register(r'list_diagnosis', views.DiagnosisViewSet)

urlpatterns = [
    path("auth/signup", views.SignUpView.as_view(), name="signUp"),
    path('auth/signin', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('diagnosis/', views.DiagnosisList.as_view(), name='diagnosis-list')
    ]

urlpatterns += router.urls