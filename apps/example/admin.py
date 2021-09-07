from django.contrib import admin

from .models import Payee, Payment


@admin.register(Payee, Payment)
class ExampleAdmin(admin.ModelAdmin):
    pass
