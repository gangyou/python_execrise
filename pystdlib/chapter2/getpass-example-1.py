import getpass

user = getpass.getuser()
pwd = getpass.getpass("Enter password for user %s" % user)

print user, pwd