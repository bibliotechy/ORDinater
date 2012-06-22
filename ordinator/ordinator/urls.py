from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
 from django.contrib import admin
 admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ordinator.views.home', name='home'),
    # url(r'^ordinator/', include('ordinator.foo.urls')),
      url(r'^contest/(?P<contest>\w+)/$','list_options'),
      url(r'^contest/(?P<contest>\w+)/$','ballot'),
      url(r'^contest/(?P<contest_id>\d+)/vote/$','vote'),
      url(r'^contest/(?P<contest_id>\d+)/result/$','results'),
      url(r'^contest/(?P<contest_id>\d+)/option/(?P<option_id>\d+)/$','option'),
      url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
      url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    ...
    url(r'', include('social_auth.urls')),
    ...
)
