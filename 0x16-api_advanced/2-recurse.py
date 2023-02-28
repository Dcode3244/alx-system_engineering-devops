#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


titles = []


def recurse(subreddit, hot_list=[]):
    """
        returns the list containing titles of all hot articles
        for a given subreddit.
    """
    if len(hot_list):
        after = hot_list[0]
    else:
        after = ""
    url = "https://www.reddit.com/r/{}/hot.json?{}".format(subreddit, after)
    headers = {"User-Agent": "ubuntu:api_advanced:v1.0.0 (by /u/dcode3244)"}
    params = {'limit': '99'}
    res = requests.get(url, headers=headers,
                       allow_redirects=False,
                       params=params)
    if res.status_code != 200:
        return
    topics = res.json().get('data').get('children')
    for topic in topics:
        titles.append(topic.get('data').get('title'))

    after = res.json().get('data').get('after')
    h_list = [("after={}".format(after))]
    if after is None:
        return titles
    return recurse(subreddit, h_list)
