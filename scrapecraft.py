from BeautifulSoup import BeautifulSoup as Soup
import re
import urllib2
hpl = urllib2.urlopen(urllib2.Request("http://www.hplovecraft.com/writings/texts/")).read()
hpls = Soup(hpl)
items = hpls.findAll("li")
hrefs = []
for item in items:
    try:
        hrefs.append(item.a['href'])
    except KeyError:
        continue

workurls = map(lambda f: "http://www.hplovecraft.com/writings/texts/"+f, hrefs)
with open("./hplcorpus.txt", 'a') as corpus:
    for url in workurls:
        print("opening %s" % url)
        storysoup = Soup(urllib2.urlopen(urllib2.Request(url)).read())
        print(storysoup.title.text)
        storytext = storysoup.findAll('div')[1].text
        formatted_storytext = re.sub("\n", " ", storytext)
        formatted_storytext = re.sub("\.", ". ", formatted_storytext)
        formatted_storytext = re.sub("  ", " ", formatted_storytext)
        formatted_storytext = re.sub("(&rdquo;|&ldquo;)", "\" ", formatted_storytext)
        formatted_storytext = re.sub("(&rsquo;|&lsquo;)", "' ", formatted_storytext)
        formatted_storytext = re.sub("&mdash;", " -- ", formatted_storytext)
        formatted_storytext = re.sub("&nbsp;", "", formatted_storytext)
        formatted_storytext = re.sub("&mdash;", " -- ", formatted_storytext)
        print(formatted_storytext[:5000])
        corpus.write(storytext+" ")
