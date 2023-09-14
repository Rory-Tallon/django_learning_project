from django.urls import path

from . import views

app_name="price_collector"
urlpatterns = [
    path("", views.index, name="index"),
    path("collect_data/", views.collect_data, name="collect_data")
]
