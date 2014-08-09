from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gcompris_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^schoolbus/', include('schoolbus.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
