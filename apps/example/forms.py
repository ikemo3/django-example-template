from django.db.models import Q
from django.forms import ModelChoiceField, ModelForm

from .models import Payee, Payment


class PaymentAddForm(ModelForm):
    payee = ModelChoiceField(label="支払先", queryset=Payee.objects.filter(is_active=True))

    class Meta:
        model = Payment
        fields = ("date", "payee", "amount")


class PaymentEditForm(ModelForm):
    payee = ModelChoiceField(label="支払先", queryset=Payee.objects.none())

    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance=instance, *args, **kwargs)
        self.fields["payee"].queryset = Payee.objects.filter(Q(is_active=True) | Q(id=instance.payee_id))

    class Meta:
        model = Payment
        fields = ("date", "payee", "amount")
