from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('<int:pk>/', views.product_detail_page, name="product_detail")
]