from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    ShortenView,
    SignUpView,
    ShortenDetailView,
    DeleteView,
    CompleteDetailView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", obtain_auth_token, name="login"),
    path("shorten/", ShortenView.as_view(), name="shorten"),
    path("shorten/<str:short_code>/", ShortenDetailView.as_view(), name="detail"),
    path("shorten/delete/<str:short_code>/", DeleteView.as_view(), name="delete"),
    path("shorten/<str:short_code>/stats/", CompleteDetailView.as_view(), name="stats"),
]
