#!/usr/bin/python3
"""a module recursively requests Reddit API to get data"""
import requests


def recurse(subreddit, hot_list=[], after=25):
    """a function prints titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    header = {'User-Agent': 'Reddit API test'}
    param = {'after': after}
    response = requests.get(url, headers=header, allow_redirects=False,
                            params=param)
    dict = response.json()
    if dict.get("error", 200) == 404:
        return None
    if after is None:
        return hot_list
    l_list = dict.get("data").get("children")
    for dic in l_list:
        hot_list.append(dic.get("data").get("title"))
    pa = dict.get("data").get("after")
    return recurse(subreddit, hot_list, pa)
