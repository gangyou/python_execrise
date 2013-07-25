from django.conf.urls import patterns, include, url

urlpatterns = patterns('books.views',
	url(r'author/add$', 'forms')
)