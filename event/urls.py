from django.conf.urls import url
from event import views
from django.urls import path

app_name = 'event'
urlpatterns = [
    url(r'^$', views.EventListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='detail'),
    url(r'^create/(?P<pk>\d+)/$', views.EventCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.EventUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.EventDeleteView.as_view(), name='delete'),
]
