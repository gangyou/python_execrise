from django.forms import ModelForm
from books.models import FormAuthor, FormBook

class AuthorForm(ModelForm):
	class Meta:
		model = FormAuthor
		fields = ('name', 'title')


class BookForm(ModelForm):
	class Meta:
		model = FormBook

