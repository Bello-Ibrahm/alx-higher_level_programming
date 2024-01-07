#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response.
"""


if __name__ == "__main__":
    from sys import argv
    import urllib.request

    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
