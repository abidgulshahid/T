from django.urls import path

from tailer.views.auth import login

urlpatterns = [
    path('', login.LoginView.as_view(), name='index_view'),
]