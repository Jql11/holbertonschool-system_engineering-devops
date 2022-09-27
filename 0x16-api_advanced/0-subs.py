#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-agent': 'JQL 0x16'}).json()
    subscribers = response.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
