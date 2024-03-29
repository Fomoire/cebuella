from django.conf.urls.defaults import patterns, include, url
from cebuella.ants.queen import queen
from cebuella.pavo.views import pavo
from cebuella.pavo.tables import tables
from cebuella.ants.parrot import parrot
from cebuella.ants.views import maine
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', maine),
    url(r'^pavo/', pavo),
    url(r'^queen/', queen),
    url(r'table/(\d{1,2})/$', tables),
    url(r'^parrot/', parrot),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     
)
