from django.contrib import admin
from event.models import Event, Participant
# Register your models here.
from .models import Post

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Participant)
