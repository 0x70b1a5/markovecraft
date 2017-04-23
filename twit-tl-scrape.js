var st = require('scrape-twitter')
var fs = require('fs')

var username = "ctrlcreep"
var tl = new st.TimelineStream(username, { retweets: false, replies: true })

var tweets = []
while (true) {
  var line = tl.read()
  if (!line) break;
  tweets.push(line.text)
}

fs.writeFile(`sources/${username}.txt`, tweets.join("\n").replace(/@[a-zA-Z0-9_]+/, ""), (err)=>console.log(err));
