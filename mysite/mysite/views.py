from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import MySQLdb

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
	next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('dateapp/hours_ahead.html', locals())

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))