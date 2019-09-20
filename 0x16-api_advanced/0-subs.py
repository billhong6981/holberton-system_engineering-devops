#!/usr/bin/python3
"""my first Reddit API request"""
import requests


def number_of_subscribers(subreddit):
    """the function return the number of subcribers"""
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    header = {'User-Agent': 'Reddit API test'}

    response = requests.get(url, headers=header, allow_redirects=False)
    dict = response.json()
    if dict.get("error", 200) == 404:
        return 0
    return dict.get("data").get("children")[0].get("data")\
        .get("subreddit_subscribers")
