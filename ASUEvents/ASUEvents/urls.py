from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
    url(r'^index.html$', include('home.urls')),
    url(r'^manager/', include('managers.urls')),
    url(r'^event/(?P<eventid>[0-9]{4})/$', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
