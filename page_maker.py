from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):
	in_page = False
	def __init__(self):
		ContentHandler.__init__(self)

	def startElement(self, name, attrs):
		if name == 'page':
			self.in_page = True
			self.out = open(attrs['name'] + '.html', 'w')
			self.out.write('<html><head>\n')
			self.out.write('<title>%s</title>' % attrs['title'])
			self.out.write('</head><body>')
		elif self.in_page:
			self.out.write('<' + name)
			for key, val in attrs.items():
				self.out.write(' %s="%s"' % (key,val))
			self.out.write('>')

	def endElement(self, name):
		if name == 'page':
			self.in_page = False
			self.out.write('</body></html>')
			self.out.close()
		elif self.in_page:
			self.out.write('</%s>' % name)

	def characters(self, string):
		if self.in_page:
			self.out.write(string)

parse('website.xml', PageMaker())
