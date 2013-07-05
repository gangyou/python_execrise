from django import template
from books.models import Book
register = template.Library()

@register.filter
def foobar(value):
	return value + ' add from filter.'

@register.tag("get_current_time")
def do_current_time(parser, token):
	try:
		tags = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	format_string = tags[1][1:-1]
	var_name = tags[-1]
	return CurrentTimeNode(format_string, var_name)

import datetime

class CurrentTimeNode(template.Node):
	def __init__(self, format_string, var_name):
		self.format_string, self.var_name = format_string, var_name

	def render(self, context):
		now = datetime.datetime.now()
		context[self.var_name] = now.strftime(self.format_string)
		return ''

@register.tag('upper')
def do_upper(parser, token):
	nodelist = parser.parse(('endupper',))
	parser.delete_first_token()
	return UpperNode(nodelist)

class UpperNode(template.Node):
	def __init__(self, nodelist):
		self.nodelist = nodelist

	def render(self, context):
		output = self.nodelist.render(context)
		return output.upper()
		
@register.simple_tag
def current_time(format_string):
	try:
		return datetime.datetime.now().strftime(format_string)
	except UnicodeEncodeError:
		return ''

@register.inclusion_tag('result_snippet.html')
def books_for_author(author):
	books = Book.objects.filter(authors__id=author)
	return { 'books' : books }