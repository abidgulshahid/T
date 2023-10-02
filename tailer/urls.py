from django.urls import path

from tailer.views.auth import login, register, dashboard
from tailer.views.auth.dashboard import logout

urlpatterns = [
    path('', login.LoginView.as_view(), name='index_view'),
    path('register/', register.RegisterView.as_view(), name='signup_view'),
    path('dasboard/',dashboard.Dashboard.as_view(), name='dashboard_view'),
    path('logout/',dashboard.LogoutView.as_view(), name='logout_view'),
]