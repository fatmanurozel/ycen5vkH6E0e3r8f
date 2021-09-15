import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://twitter.com/search?q=request%20for%20startup&src=recent_search_click')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)

import sys

stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w")
sys.stdout.close()
sys.stdout=stdoutOrigin

