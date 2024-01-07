#!/usr/bin/python3
""" Script tthat takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header """


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
