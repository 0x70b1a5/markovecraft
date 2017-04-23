import json
import sys

d = json.JSONDecoder()
filename = sys.argv[1]
f=open(filename)
g=open("sources/"+filename,"w")
tweets = f.read().split("\n")
for t in tweets:
    text = d.decode(t)['text']
    g.write(text+"\n")
