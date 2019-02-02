
#These are the libraries needed, urllib is whatI used to read the source code of the website

import urllib2
import sys

#To find the key you had to be be a 1000th visitor, ex: 1000, 100,5000, etc., so the only thing that was neccessary was to visit it until
#the key was found

while True:
    about_page = urllib2.urlopen("http://ctf.slothparadise.com/about.php").read()    print(about_page)
    if "KEY" in about_page:
        print(about_page)
        sys.exit(0)

#first CTF ever!!
