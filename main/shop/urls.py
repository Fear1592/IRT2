from django.urls import path
from .views import *

urlpatterns = [
    path('shop_category/create/', CategoryCreateView.as_view()),
    path('shop_category/all/', CategoryListView.as_view()),
    path('shop_category/detail/<int:pk>/', CategoryDetailView.as_view()),
    path('shop/create/', ProductCreateView.as_view()),
    path('shop/all/', ProductListView.as_view()),
    path('shop/detail/<int:pk>/', ProductDetailView.as_view()),
]
