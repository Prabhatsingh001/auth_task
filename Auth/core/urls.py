from django.urls import path
from .views import login_view,signup_view,dashboard_view,logout_view

urlpatterns = [
    path("", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
]