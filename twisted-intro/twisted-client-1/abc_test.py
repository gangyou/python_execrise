import sys, subprocess, urllib
def getSpeech(phrase):
	googleApiUrl = 'http://translate.google.com/translate_tts?tl=en&'
	param = { 'q': phrase}
	data = urllib.urlencode(param)
	googleApiUrl += data
	return googleApiUrl

print getSpeech('hello world')