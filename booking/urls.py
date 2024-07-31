from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import trip_list, create_trip, update_trip, delete_trip, TripViewSet

main_router = DefaultRouter()
main_router.register('api', TripViewSet)

urlpatterns = [
    path('', trip_list, name='trip_list'),
    path('new/', create_trip, name='create_trip'),
    path('<int:pk>/update/', update_trip, name='update_trip'),
    path('<int:pk>/delete/', delete_trip, name='delete_trip'),
] + main_router.urls
