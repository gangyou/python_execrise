import locale, time

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
	print '%20s: %s' % (name, time.strftime(locale.nl_langinfo(locale.D_T_FMT)))