from django.urls import path

from . import views

urlpatterns = [
    # Home
    path("", views.store, name="store"),# store
    # Single Product / Product Detail
    path("product/<slug:slug>/", views.product_info, name="product_info"),
    # Category list
    path("category/<slug:category_slug>/", views.list_category, name="list_category"),
]