from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)

if 'django_cas' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^accounts/login/$', 'django_cas.views.login'),
        (r'^accounts/logout/$', 'django_cas.views.logout'),
    )

urlpatterns += patterns('',
    url(r'^$', 'timer.views.show_timer'),
    url(r'^set/?$', 'timer.views.set_timer'),
    url(r'^state/?$', 'timer.views.state'),
    url(r'^t/(?P<slug>[^/]*)/?$', 'timer.views.show_timer'),
    url(r'^t/(?P<slug>[^/]*)/set/?$', 'timer.views.set_timer'),
    url(r'^t/(?P<slug>[^/]*)/state/?$', 'timer.views.state'),
)
