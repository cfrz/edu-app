from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^edu/', include('edu.urls')),
    # tinymce is the RTF editor for model fields
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
