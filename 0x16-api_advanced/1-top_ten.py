#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-agent': 'JQL 0x16'}).json()
    posts = response.get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data').get('title'))
    if not posts:
        print(None)
