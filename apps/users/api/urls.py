from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/users', views.UsersList.as_view()),
    path('api/v1/houses', views.HouseAPIView.as_view()),
]
