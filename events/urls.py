from django.conf.urls import patterns, url, include
from events import views

urlpatterns = patterns('',
	url(r'^tonight/$', views.tonight, name='ev_tonight'),
)
