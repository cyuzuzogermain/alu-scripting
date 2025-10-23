#!/usr/bin/python3

#!/usr/bin/python3
"""
Reddit Top Ten Hot Posts Module

This module provides a function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.

Usage:
    top_ten('python')
"""

import requests

def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts of a subreddit.

    This function queries the Reddit API for the given subreddit. If the
    subreddit is invalid or cannot be accessed, it prints None. It avoids
    following redirects to handle invalid subreddits properly.

    Args:
        subreddit (str): Name of the subreddit to query (e.g., 'python').

    Returns:
        None
    """
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
        # Handle network errors gracefully
        print(None)
