from django.shortcuts import render
from django.views.generic import TemplateView


def func(request, *args, **kwargs):
    return render(request, "example.html", {})


class IndexView(TemplateView):
    template_name = "index.html"


class VanillaTemplateView(TemplateView):
    template_name = "example.html"


class PostSupportView(TemplateView):
    template_name = "example.html"

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class PostWithHttpMethodNamesView(TemplateView):
    http_method_names = ["get"]
    template_name = "example.html"

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class NoHttpMethodNamesView(TemplateView):
    template_name = "example.html"


class HttpMethodNamesView(TemplateView):
    http_method_names = ["get"]
    template_name = "example.html"
