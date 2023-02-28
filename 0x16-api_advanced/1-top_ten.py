#!/usr/bin/python3
"""
queries the Redit API and prints the titles of the first 10
hot posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        prints the ritles of the first 10 hot posts
        listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:api_advanced:v1.0.0 (by /u/dcode3244)"}
    params = {'limit': '10'}
    res = requests.get(url, headers=headers,
                       allow_redirects=False,
                       params=params)
    if res.status_code != 200:
        print('None')
        return
    topics = res.json().get('data').get('children')
    [print(topic.get('data').get('title')) for topic in topics]
