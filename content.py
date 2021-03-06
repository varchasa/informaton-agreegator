import urllib, os, requests, datetime, subprocess

import praw, pprint


import feedparser

from nsetools import Nse

reddit = praw.Reddit(client_id='XXXXXXXX',
                     client_secret='XXXXXXXXXXXXXX',
                     grant_type_access='client_credentials',
                     user_agent='script/1.0')

class News:
    def Indian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"
        )
        print("Today's News: ")
        for i in range(0, 10):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("------News Link--------")
            print(entry.link)
            print("###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')

    def times_ofindia(self):
        newsfeed=feedparser.parse("https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms")
        print("todays times of india news : ")
        for i in range(0,10):
            entry=newsfeed.entries[i]
            print(entry.title)
            print("------- News Link --------")
            print(entry.link)
            print("##############\n")
        print("-------------------------------------------------------------------------------------------------")
class Medium:
    def medium_programming(self):
        feed = feedparser.parse('https://medium.com/feed/tag/programming')

        print('Programming today : ')
        print("****************")
        for i in range(0,10):
            print("pr ",i)
            entry = feed.entries[i]
            print(entry.title)
            print('URL : ' + entry.link)
            print("\n***********\n")

    def medium_python(self):
        feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
        print("Python Today: ")
        for i in range(0,10):
            print("python ",i)
            entry = feed_python.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')

    def medium_developer(self):
        feed_developer = feedparser.parse(
            "https://medium.com/feed/tag/developer"
        )
        print("Developer News Today: ")
        for i in range(5):
            entry = feed_developer.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')




# objects inititalization
# reddit_object = Reddit()
News_object = News()
Medium_object = Medium()


if __name__ == "__main__":
    print("1. NDTV News\n2. Times of India news\n3. Python Articles\n4. Programming Articles\n5. Developer Articles\n")
    n=int(input("enter ur choice\n"))
    if(n==1):
        News_object.Indian_News()
    elif(n==2):
        News_object.times_ofindia()
    elif(n==3):
        Medium_object.medium_python()
    elif(n==4):
        Medium_object.medium_programming()
    elif(n==5):
        Medium_object.medium_developer()
    else:
        print("please enter valid choice")
    
