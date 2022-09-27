#!/usr/bin/python3
"""
2-recursive
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    use recursive function
    return a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={'User-agent': 'JQL 0x16'},
                            params={'after': after}).json()
    data = response.get('data', {})
    posts = data.get('children', [])
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after = data.get('after')
    if not after:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
