from django.urls import path

from apps.example import views_example

urlpatterns = [
    path("", views_example.ExampleView.as_view(), name="example"),
]
