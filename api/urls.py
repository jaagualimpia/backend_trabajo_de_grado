from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'diagnosis', views.DiagnosisViewSet)

urlpatterns = [
    path("auth/signin", views.AuthenticationView.as_view(), name="signin"),
    path("auth/signUp", views.SignUpView.as_view(), name="signUp")
]

urlpatterns += router.urls