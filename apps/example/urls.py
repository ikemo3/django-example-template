from django.urls import path

from apps.example import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("func/", views.func, name="func"),
    path("vanilla/", views.VanillaTemplateView.as_view(), name="vanilla"),
    path("post_support/", views.PostSupportView.as_view(), name="post-support"),
    path(
        "post_with_http_method_names/", views.PostWithHttpMethodNamesView.as_view(), name="post-with-http-method-names"
    ),
    path("no_http_method_names/", views.NoHttpMethodNamesView.as_view(), name="no-http-method-names"),
    path("http_method_names/", views.HttpMethodNamesView.as_view(), name="http-method-names"),
]
