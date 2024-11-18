from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="store"),# store
    path("product/<slug:slug>/", views.product_info, name="product_info"),# product_info
]