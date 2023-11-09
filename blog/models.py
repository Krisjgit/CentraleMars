from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone


class Room(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    available = models.BooleanField(default=False)
    campus = models.CharField(default="Marseille", max_length=128)
    capacity = models.IntegerField(default=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    race = models.CharField(default="Earth", max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    photo = models.CharField(max_length=400)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
