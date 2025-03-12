
from django.contrib import admin
from django.urls import path
from django.conf import settings
from accounts.views import SignInView, SignUpView, UserView


urlpatterns = [
    path("signin", SignInView.as_view()),
    path('signup', SignUpView.as_view()),
    path('me', UserView.as_view()),
]
