from django.urls import path

from apps.example import views

urlpatterns = [
    path("", views.PaymentListView.as_view(), name="list"),
    path("add/", views.PaymentAddView.as_view(), name="add"),
    path("edit/<int:pk>", views.PaymentEditView.as_view(), name="edit"),
]
