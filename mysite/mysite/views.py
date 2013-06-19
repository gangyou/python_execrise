from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	assert False
	html = "In %s hour(s), it will be %s." % (offset, dt)
	return HttpResponse(html)