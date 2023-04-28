#!/usr/bin/python3
"""
Python script that takes in a letter
Sends a POST request to http://0.0.0.0:5000/search_user
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    p = requests.post(url, ({'q':q}))
    try:
        response = p.json()
        if len(response) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
