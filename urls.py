from django.conf.urls.defaults import patterns, include, url
from cebuella.ants.queen import queen
from cebuella.pavo.views import pavo, chart
from cebuella.pavo.tables import tables
from cebuella.pavo.fr_pavo import fr_pavo
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
    url(r'^chart/', chart),
    url(r'^freq/', fr_pavo),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     
)
