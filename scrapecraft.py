from bs4 import BeautifulSoup as Soup
import re
import urllib
hpl = urllib.request.urlopen("http://www.hplovecraft.com/writings/texts/").read()
hpls = Soup(hpl, "lxml")
items = hpls.findAll("li")
hrefs = []
for item in items:
    try:
        hrefs.append(item.a['href'])
    except KeyError:
        continue

workurls = map(lambda f: "http://www.hplovecraft.com/writings/texts/"+f, hrefs)
with open("./hplcorpus.txt", 'w') as corpus:
    for url in workurls:
        print("opening %s" % url)
        storysoup = Soup(urllib.request.urlopen(url).read())
        print(storysoup.title.text)
        storytext = storysoup.findAll('div')[1].text
        print(storytext[:5000])
        corpus.write(str(storytext))
