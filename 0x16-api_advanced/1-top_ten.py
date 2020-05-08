#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10 hot
"""

import requests


def top_ten(subreddit):
    head = {'user-agent': 'X-Modhash'}
    page = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(page, headers=head, allow_redirects=False,
                     params={'limit': 10})
    r_json = r.json()
    if r.status_code == 404:
        print(None)
    else:
        for display in r_json['data']['children']:
            print(display['data']['title'])
