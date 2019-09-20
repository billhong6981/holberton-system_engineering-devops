#!/usr/bin/python3
"""a module recursively requests Reddit API to get data"""
import requests


def sort_func(word_list, hot_list, dict_wc):
    """sorted words occurence times in desc order"""
    if not word_list:
        print
        return None
    if not hot_list:
        print
        return None
    for word in word_list:
        dict_wc[word] = 0
        for title in hot_list:
            n = title.lower().count(word)
            dict_wc[word] += n
    dict_wc = {key: value for key, value in dict_wc.items() if value}
    if not dict_wc:
        print
        return None
    for key in sorted(dict_wc, key=dict_wc.get, reverse=True):
        print("{}: {}".format(key, dict_wc[key]))
    return dict_wc


def count_words(subreddit, word_list=[], hot_list=[], after=25):
    """a function counts the word occurence in the hot articles
    for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    header = {'User-Agent': 'Reddit API test'}
    param = {'after': after}
    response = requests.get(url, headers=header, allow_redirects=False,
                            params=param)
    try:
        dict = response.json()
    except:
        print
        return None
    if dict.get("error", 200) == 404:
        return None
    if after is None:
        dict_wc = sort_func(word_list, hot_list, dict_wc={})
        return dict_wc
    l_list = dict.get("data").get("children")
    for dic in l_list:
        hot_list.append(dic.get("data").get("title"))
    pa = dict.get("data").get("after")
    return count_words(subreddit, word_list, hot_list, pa)
