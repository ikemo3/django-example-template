from django.db import models
from django.db.models import Case, CharField, IntegerField, PositiveSmallIntegerField, Value, When


def qs_custom_order(qs, key: str, sort_order: tuple):
    cases = []
    for index, value in enumerate(sort_order):
        when_params = {
            key: value,
            "then": Value(index),
        }
        cases.append(When(**when_params))

    return qs.annotate(custom_order=Case(*cases, output_field=IntegerField())).order_by("custom_order")


class TaskStatus(models.IntegerChoices):
    TODO = 0, "TODO"
    DONE = 1, "完了"
    CANCELLED = 2, "キャンセル"
    WIP = 3, "WIP"

    @staticmethod
    def sort_order():
        return (
            TaskStatus.TODO,
            TaskStatus.WIP,
            TaskStatus.DONE,
            TaskStatus.CANCELLED,
        )


class TaskQuerySet(models.QuerySet):
    def __init__(self, model=None, query=None, using=None, hints=None):
        super().__init__(model, query, using, hints)

    def order_by_status(self):
        return qs_custom_order(self, key="status", sort_order=TaskStatus.sort_order())


class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def order_by_status(self):
        return self.get_queryset().order_by_status()


class Task(models.Model):
    name = CharField(max_length=100, verbose_name="タスク名")
    status = PositiveSmallIntegerField(verbose_name="ステータス", choices=TaskStatus.choices)

    objects = TaskManager()

    def __str__(self):
        return f"{self.name}: {TaskStatus(self.status).label}"
