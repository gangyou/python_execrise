import datetime

today = datetime.date.today()
print today
print 'ctime : ', today.ctime()
print 'tuple : ', today.timetuple()
print 'ordinal : ', today.toordinal()
print 'Year:' , today.year
print 'Mon : ', today.month
print 'Day : ', today.day