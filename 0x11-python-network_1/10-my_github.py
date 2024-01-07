#!/usr/bin/python3
""" Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get(url, auth=auth)
    print(req.json().get("id"))
