#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=data)

    try:
        re_json = req.json()
        if re_json:
            print("[{}] {}".format(re_json.get('id'), re_json.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
