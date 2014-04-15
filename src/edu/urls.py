from django.conf.urls import patterns, include, url
from .views import home_page, article_view, pathogen_view, isolation_view, pathtype_view


urlpatterns = patterns('',
    url(r'^home/', 'edu.views.home_page'),
    url(r'^get/(?P<article_id>\w+)/$', 'edu.views.article_view'),
    url(r'^iso/(?P<isolation_id>\w+)/$', 'edu.views.isolation_view'),
    url(r'^pathogen/(?P<pathogen_id>\w+)/$', 'edu.views.pathogen_view'),
    url(r'^hai/(?P<hai_id>\w+)/$', 'edu.views.hai_view'),
    url(r'^pathtype/(?P<pathtype_id>\w+)/$', 'edu.views.pathtype_view'),
    url(r'^ppe/(?P<ppe_id>\w+)/$', 'edu.views.ppe_view'),
                       )