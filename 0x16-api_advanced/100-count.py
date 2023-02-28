#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.).
"""
import requests


def count_words(subreddit, word_list, hot_list=[], key_words={}):
    """
        prints sorted count of given keywords from a given subreddit
        hot titles.
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
        title = topic.get('data').get('title').lower().split()
        for word in word_list:
            word = word.lower()
            num = 0
            if word in title:
                for t in title:
                    if word == t:
                        num += 1
            if key_words.get(word) is None:
                if num != 0:
                    key_words[word] = num
            else:
                key_words[word] = key_words[word] + num

    after = res.json().get('data').get('after')
    h_list = [("after={}".format(after))]
    if after is None:
        if len(key_words) == 0:
            return
        key_words = sorted(key_words.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in key_words]
    else:
        count_words(subreddit, word_list, h_list, key_words)
