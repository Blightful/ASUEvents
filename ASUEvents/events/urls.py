from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('',
    url(r'^$', views.EventView.as_view(), name='event'),
)