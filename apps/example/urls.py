from django.urls import path

from apps.example import views

urlpatterns = [
    path("", views.ExampleView.as_view(), name="example"),
]
