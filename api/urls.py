from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'diagnosis', views.DiagnosisViewSet)

urlpatterns = [
    path("auth/signin", views.AuthenticationView.as_view(), name="signIn"),
    path("auth/signup", views.SignUpView.as_view(), name="signUp"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls