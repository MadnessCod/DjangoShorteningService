from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import ShortenView, SignUpView, ShortenDetailView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", obtain_auth_token, name="login"),
    path("shorten/", ShortenView.as_view(), name="shorten"),
    path("shorten/<str:short_code>/", ShortenDetailView.as_view(), name="detail"),
]
