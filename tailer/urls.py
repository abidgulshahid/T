from django.urls import path

from tailer.views.auth import login, register

urlpatterns = [
    path('', login.LoginView.as_view(), name='index_view'),
    path('register/', register.RegisterView.as_view(), name='signup_view'),
]