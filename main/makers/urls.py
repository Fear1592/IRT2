from django.urls import path
from .views import *

urlpatterns = [
    path('produced/all/', ProducedListView.as_view()),
    path('produced/detail/<int:pk>/', ProducedDetailView.as_view()),

]
