import locale

sample_locales = [
	('USA', 'en_US'),
	('France', 'fr_FR'),
	('China', 'zh_CN'),
	('Spain', 'es_ES'),
	('Portugal', 'pt_PT'),
	('Porland', 'pl_PL'),
	]

for name, loc in sample_locales:
	locale.setlocale(locale.LC_ALL, loc)
	print '%20s: %s' % (name, locale.currency(1234.56))