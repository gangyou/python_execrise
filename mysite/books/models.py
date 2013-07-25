from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	headshot = models.ImageField(upload_to='author_headshot')

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __unicode__(self):
		return self.title

TITLE_CHOICES = (
	('MR', 'Mr.'),
	('MRS', 'Mrs.'),
	('MS', 'Ms.'),
)

class FormAuthor(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=3, choices=TITLE_CHOICES)
	birth_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class FormBook(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)