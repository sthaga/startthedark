from django.conf.urls.default import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(''
        (r'^events/$', include('events.urls')),
	(r'^admin/(.*)', admin.site.root),
)
