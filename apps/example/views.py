from django.views.generic import CreateView, ListView, UpdateView

from .forms import PaymentAddForm, PaymentEditForm
from .models import Payment


class PaymentListView(ListView):
    model = Payment
    template_name = "list.html"


class PaymentAddView(CreateView):
    model = Payment
    form_class = PaymentAddForm
    template_name = "add.html"


class PaymentEditView(UpdateView):
    model = Payment
    form_class = PaymentEditForm
    template_name = "edit.html"
