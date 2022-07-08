from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignInView
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import TimeAttackTokenObtainPairView
urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('sign-in', SignInView.as_view()),
    path('api/token/', TimeAttackTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
