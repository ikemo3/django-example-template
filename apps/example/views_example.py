from django.views.generic import ListView

from apps.example.models import Task


class ExampleView(ListView):
    template_name = "example.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ordered_list"] = Task.objects.order_by_status()
        return context
