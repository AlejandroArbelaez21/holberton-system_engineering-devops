#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    head = {'user-agent': 'X-Modhash'}
    page = "https://reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(page, headers=head)
    r_json = r.json()
    if r.status_code == 404:
        return 0
    else:
        return r_json["data"]["subscribers"]
