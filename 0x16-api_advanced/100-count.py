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
        title = topic.get('data').get('title').lower()
        for word in word_list:
            word = word.lower()
            num = title.count(word)
            if key_words.get(word) is None:
                if num != 0:
                    key_words[word] = num
            else:
                key_words[word] = key_words[word] + num

    after = res.json().get('data').get('after')
    h_list = [("after={}".format(after))]
    if after is None:
        if len(key_words) > 0:
            sorted_print(key_words)
        return
    count_words(subreddit, word_list, h_list, key_words)


def sorted_print(key_words):
    """ prints words with their count in descending order """
    s_key = list(key_words.keys())
    s_key.sort()
    sorted_by_key = {i: key_words[i] for i in s_key}
    s_val = sorted(sorted_by_key.items(), key=lambda x: x[1], reverse=True)
    s_val = dict(s_val)
    for key, value in s_val.items():
        print("{}: {}".format(key, value))
