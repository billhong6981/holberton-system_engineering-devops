#!/usr/bin/python3
"""the module make request from Reddits API"""
import requests


def top_ten(subreddit):
    """the function prints the titles of the first 10 hot posts"""
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    header = {'User-Agent': 'Reddit API test'}
    response = requests.get(url, headers=header, allow_redirects=False)
    dict = response.json()
    if dict.get("error", 200) == 404:
        return print("None")
    l_ist = dict.get("data").get("children")
    for dic in l_ist[0:10]:
        print(dic.get("data").get("title"))
