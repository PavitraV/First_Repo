from django.conf.urls import patterns, include, url
from django.contrib import admin
import testing

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'pavitra_v01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^testing/', include('testing.url')),
    url(r'^admin/testing/load/getSuggestions/$',testing.views.getSuggestions),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
