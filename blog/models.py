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

    def getPersons(self):
        persons = Person.objects.all()
        persons_inside = []
        for person in persons:
            if person.location.pk == self.pk:
                persons_inside.append(person)
        return persons_inside

    def updateAvailability(self):
        self.available = len(self.getPersons()) < self.capacity


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    planet = models.CharField(default="Earth", max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    photo = models.CharField(max_length=400, blank=True, default='images/profile.png')
    location = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

    def updatePlanet(self):
        campus = self.location.campus
        if campus == "Mars":
            self.planet = "Mars"
        else:
            self.planet = "Earth"

