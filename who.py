import urllib2 as request
import cookielib, urllib, urllib2, getpass

stringURL = "http://moodle.ashmanorschool.com/user/profile.php?id="
loginUrl = "https://moodle.ashmanorschool.com/login/index.php"

username= raw_input("\tusername: ")
password= getpass.getpass("\tpassword: ")



passman = urllib2.HTTPPasswordMgrWithDefaultRealm()

passman.add_password(None, loginUrl, username, password)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPBasicAuthHandler(passman),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cj),
)

urllib2.install_opener(opener)


# set headers
opener.addheaders = [
    ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                   'Windows NT 5.2; .NET CLR 1.1.4322)'))
]

try:
    req = opener.open(loginUrl)
except IOError, e:
    print "It looks like the username or password is wrong."


for i in range (100):
    url = stringURL + str(i)
    webpage = request.urlopen(url)
    webpage = webpage.read(100)
    start = webpage.find('<title>') +7
    finish = webpage.find('</title>')
    title = webpage[start:finish]
    print (str(i) + ' ' + title)