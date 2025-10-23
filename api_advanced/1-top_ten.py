#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a given subreddit."""
    headers = {'User-Agent': 'Python:TopTenScript:v1.0 (by /u/yourusername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if subreddit is valid
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            print(post['data']['title'])

    except requests.exceptions.RequestException:
        # In case of network error
        print(None)

