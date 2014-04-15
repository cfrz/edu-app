from django.conf.urls import patterns, include, url
from django.contrib import admin
# dev static serving
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    (r'^edu/', include('edu.urls')),
    # tinymce is the RTF editor for model fields
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
