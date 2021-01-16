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
        for i in range(0, 20):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("------News Link--------")
            print(entry.link)
            print("###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')

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


class StockExchange:
    def nse_stock(self):
        nse = Nse()
        print("TOP GAINERS OF YESTERDAY")
        pprint.pprint(nse.get_top_gainers())
        print("###########################################")
        print("TOP LOSERS OF YESTERDAY")
        pprint.pprint(nse.get_top_losers())
        print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


# objects inititalization
# reddit_object = Reddit()
News_object = News()
Medium_object = Medium()
StockExchange_object = StockExchange()

if __name__ == "__main__":
    News_object.Indian_News()
    Medium_object.medium_python()
    Medium_object.medium_programming()
    Medium_object.medium_developer()
    StockExchange_object.nse_stock()
    
