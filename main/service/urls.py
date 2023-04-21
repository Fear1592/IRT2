from django.urls import path
from .views import *

urlpatterns = [
    path('service_category/create/', CategoryMakersCreateView.as_view()),
    path('service_category/all/', CategoryMakersListView.as_view()),
    path('service_category/detail/<int:pk>/', CategoryMakersDetailView.as_view()),
    path('service/create/', ServiceCreateView.as_view()),
    path('service/all/', ServiceListView.as_view()),
    path('service/detail/<int:pk>/', ServiceDetailView.as_view()),
    path('service_image/create/', ServiceImageCreateView.as_view()),
    path('service_image/all/', ServiceImageListView.as_view()),
    path('service_image/detail/<int:pk>/', ServiceImageDetailView.as_view()),
]
