from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^$', views.RegisterView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='register')
)