from django.conf.urls.defaults import patterns, include, url
from cebuella.ants.queen import queen
from cebuella.pavo.views import pavo
from cebuella.pavo.tables import tables
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', pavo),
    url(r'^queen/', queen),
    url(r'table/(\d{1,2})/$', tables),
    # url(r'^Cuebella/', include('Cuebella.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     
)
