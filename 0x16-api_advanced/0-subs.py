#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns total number of subscribers of a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:api_advanced:v1.0.0 (by /u/dcode3244)"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0
    return (res.json().get('data').get('subscribers'))
