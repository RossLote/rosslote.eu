from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('rosslote.views',
    # Examples:
    url(r'^$', 'index', name='home'),
    url(r'^about/$', 'about', name='about'),
    url(r'^projects/$', 'index', name='projects'),
    url(r'^cv/$', 'cv', name='cv'),
    url(r'^contact/$', 'index', name='contact'),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia', app_name='zinnia')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
