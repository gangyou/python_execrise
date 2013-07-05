from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book
from django.core.mail import send_mail


def search_form(request):
	return render_to_response('search_form.html', {'hello' : 'world'})

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books': books, 'query': q})
	return render_to_response('search_form.html', {'errors': errors, 'hello': 'world'})

def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			# send mail
			return HttpResponseRedirect('/contact/thanks')
	return render_to_response('contact_form.html', {'errors': errors})

def thanks(request):
	return render_to_response('contact_thanks.html')