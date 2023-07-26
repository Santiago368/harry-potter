from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(
    'houses',
    views.HouseModelViewSet,
    basename="house"
)


urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('api/v1/users', views.UsersList.as_view()),
    # path('api/v1/houses', views.HouseAPIView.as_view()),
    # path('api/v1/houses/<int:pk>/', views.HouseAPIView.as_view()),
]
