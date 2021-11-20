from django.urls import path
from django.contrib import admin

from .views import (
    GetUserImageListAPIView,
    RetrieveDetailForUserImageAPIView,
    CreateUserImageAPIView,
    GetUserDataImageListAPIView)

app_name = 'user_card'

urlpatterns = [
    path("get", GetUserImageListAPIView.as_view(), name="get"),
    path("<int:pk>", RetrieveDetailForUserImageAPIView.as_view(), name="retrieve"),
    path("create", CreateUserImageAPIView.as_view(), name="create"),
    path("getuserdata", GetUserDataImageListAPIView.as_view(), name="get-User-Data")
]
 