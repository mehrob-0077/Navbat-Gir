from django.urls import path
from .views import *

urlpatterns = [
    path("", register_view, name="register"),
    path("login/",login_view,name="login"),
    path("home/", home_view, name="home"),
    path("logout/", logout_view, name="logout"),
    path("confirm/<str:token>/", confirm_email_view, name="confirm_email"),
]
