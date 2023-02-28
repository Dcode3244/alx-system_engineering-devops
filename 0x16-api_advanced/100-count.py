#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], key_words={}):
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
        title = topic.get('data').get('title').lower()
        for word in word_list:
            num = title.lower().count(word.lower())
            if key_words.get(word) is None:
                if num != 0:
                    key_words[word] = num
            else:
                key_words[word] = key_words[word] + num

    after = res.json().get('data').get('after')
    h_list = [("after={}".format(after))]
    if after is None:
        count = [num for num in key_words.values()]
        count.sort(reverse=True)
        keys = (list(key_words.keys()))
        keys.sort()
        sorted_key_words = {i: key_words[i] for i in keys}
        for n in count:
            for k, v in sorted_key_words.items():
                if v == n:
                    print("{}: {}".format(k, v))
        return
    count_words(subreddit, word_list, h_list, key_words)
