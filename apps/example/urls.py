from apps.example import views
from django.urls import path

urlpatterns = [
    path("", views.ExampleView.as_view(), name="example"),
]
