from django.db import models
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    event_name = models.CharField(max_length=256)
    venue = models.CharField(max_length=256)
    event_date = models.DateField()
    event_description = models.TextField(max_length=500)
    event_duration = models.IntegerField()
    event_organiser = models.CharField(max_length=256)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("event:detail", kwargs={'pk': self.pk})


class Participant(models.Model):
    name = models.CharField(max_length=256)
    college_name = models.CharField(max_length=256)
    contact_number = models.CharField(max_length=10)
    event_name = models.ForeignKey(Event, related_name='participant', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
