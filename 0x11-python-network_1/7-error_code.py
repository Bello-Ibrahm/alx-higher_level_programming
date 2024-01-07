#!/usr/bin/python3
""" Script takes takes in a URL, sends a request to the URL
and displays the body of the response."""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
