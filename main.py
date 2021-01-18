from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
import urllib, os, requests, datetime, subprocess
import praw, pprint
import feedparser
from nsetools import Nse
reddit = praw.Reddit(client_id='XXXXXXXX',
                     client_secret='XXXXXXXXXXXXXX',
                     grant_type_access='client_credentials',
                     user_agent='script/1.0')

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/news")
def news():
    title=[]
    link=[]
    newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news")
    for i in range(0, 10):
        entry = newsfeed.entries[i]
        title.append(entry.title)
    
        
        link.append(entry.link)
    return render_template('home.html',title=title,link=link)

if __name__=='__main__':
    app.run(debug=True)

