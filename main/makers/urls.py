from django.urls import path
from .views import *

urlpatterns = [
    path('makers/create/', ProducedCreateView.as_view()),
    path('makers/all/', ProducedListView.as_view()),
    path('makers/detail/<int:pk>/', ProducedDetailView.as_view()),
    path('makers_category/create/', CategoryMakersCreateView.as_view()),
    path('makers_category/all/', CategoryMakersListView.as_view()),
    path('makers_category/detail/<int:pk>/', CategoryMakersDetailView.as_view()),
    path('makers_image/create/', ProducedImageCreateView.as_view()),
    path('makers_image/all/', ProducedImageListView.as_view()),
    path('makers_image/detail/<int:pk>/', ProducedImageDetailView.as_view()),

]
