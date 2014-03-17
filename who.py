import urllib.request as request
tringURL = "http://moodle.ashmanorschool.com/user/profile.php?id="

for i in range (10000):
    url = stringURL + i
    webpage = request.urlopen(url)
    start = webpage.find(<title>) +7
    finish = </title>
    title = webpage[start:finish]
    print (title)
