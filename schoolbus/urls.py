from django.conf.urls import patterns, url

from schoolbus import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /profile/<id>/
    url(r'^profile/(?P<profile_id>\d+)/$', views.profile, name='profile'),
    # ex: /profiles/<uuid>/
    url(r'^profiles/(?P<teacher_uuid>[0-9A-Fa-f]+)/$', views.profiles, name='profiles'),
    # ex: /registerApplication/<uuid>/
    url(r'^getProfileByLogin/(?P<teacher_uuid>[0-9A-Fa-f]+)/(?P<login>\w+)$',
        views.getProfileByLogin, name='getProfileByLogin'),
)
