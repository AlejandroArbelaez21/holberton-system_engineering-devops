#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and
returns a list containing the titles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    head = {'user-agent': 'X-Modhash'}
    page = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(page, headers=head, params={'after': after},
                     allow_redirects=False)
    r_json = r.json()
    if r.status_code == 404:
        return (None)
    else:
        for display in r_json['data']['children']:
            hot_list.append(display['data']['title'])
        if r_json['data']['after'] is None:
            return hot_list
        else:
            return (recurse(subreddit, hot_list, r_json['data']['after']))
