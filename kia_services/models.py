from enum import Enum

from django.db import models
from jsonfield import JSONField


# Create your models here.
from KIA_auth.models import Profile


class KIAService(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, null=True)
    # TODO: let user insert html for details
    details = models.TextField()
    image_url = models.URLField(null=True)

    def __str__(self):
        return self.name


class KIAServiceField(models.Model):
    boolean_field = 1
    char_field = 2
    choice_field = 3
    date_field = 5
    date_time_field = 6
    decimal_field = 7
    email_field = 9
    file_field = 10
    integer_field = 13
    multiple_choice_field = 14
    TYPE_CHOICES = (
        (boolean_field, "فیلد صحیح و غلط"),
        (char_field, "فیلد متنی"),
        (choice_field, "فیلد انتخاب یک گزینه"),
        (date_field, "فیلد تاریخ"),
        (date_time_field, "فیلد تاریخ و زمان"),
        (decimal_field, "فیلد عدد اعشاری"),
        (email_field, "فیلد ایمیل"),
        (file_field, "فیلد فایل"),
        (integer_field, "فیلد عدد صحیح"),
        (multiple_choice_field, "فیلد انتخاب چند گزینه"),
    )

    service = models.ForeignKey(KIAService, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True)
    label = models.CharField(max_length=100)
    type = models.IntegerField(choices=TYPE_CHOICES)
    optional = models.BooleanField(default=False)
    args = JSONField()

    def __str__(self):
        return format("%s: %s" % (self.service.name, self.name))


class KIATransaction(models.Model):
    registered = 1
    being_done = 2
    done = 3
    failed = 4
    STATE_CHOICES = (
        (registered, "Registered"),
        (being_done, "Being done"),
        (done, "Done"),
        (failed, "Failed")
    )

    service = models.ForeignKey(KIAService, on_delete=models.SET_NULL, null=True)
    # TODO: remove null=True from next field after passing login info in view
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    state = models.IntegerField(choices=STATE_CHOICES)
    # assigned_emp = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    data = JSONField()

    def initialize(self, service_name):
        self.state = self.registered
        self.service_name = service_name


