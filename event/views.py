from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from . import models
from django.urls import path
# Create your views here.
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'event/event_base.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'


class EventListView(ListView):
    context_object_name = 'events'
    model = models.Event


class EventDetailView(DetailView):
    context_object_name = 'event_detail'
    model = models.Event
    template_name = "event/login/event_detail.html"


class EventCreateView(CreateView):
    fields = ('event_name', 'venue', 'event_date', 'event_description', 'event_duration', 'event_organiser')
    model = models.Event


class EventUpdateView(UpdateView):
    fields = ('event_name', 'venue', 'event_date', 'event_description', 'event_duration', 'event_organiser')
    model = models.Event


class EventDeleteView(DeleteView):
    model = models.Event
    success_url = reverse_lazy("event:list")
