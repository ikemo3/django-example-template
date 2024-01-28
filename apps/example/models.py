from django.db import models
from django.db.models import BooleanField, CharField, DateField, ForeignKey, PositiveIntegerField


class Payee(models.Model):
    """支払先"""

    name = CharField(max_length=20, verbose_name="支払先名称")
    is_active = BooleanField(verbose_name="有効?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "支払先"


class Payment(models.Model):
    """支払い"""

    date = DateField(verbose_name="支払日")
    payee = ForeignKey(Payee, verbose_name="支払先", on_delete=models.PROTECT)
    amount = PositiveIntegerField(verbose_name="金額")

    def __str__(self):
        return f"{self.date} {self.payee} {self.amount}円"

    class Meta:
        verbose_name = verbose_name_plural = "支払い"
