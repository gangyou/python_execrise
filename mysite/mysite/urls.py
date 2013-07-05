from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from books import views
from contact import views as contact_views
admin.autodiscover()

urlpatterns = patterns('',
	(r'^hello/$', hello),
	(r'^time/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meta/$', display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact_views.contact),
    url(r'^contact/thanks/$', contact_views.thanks),
)
