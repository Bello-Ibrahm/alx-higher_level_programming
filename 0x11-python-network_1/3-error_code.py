#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8). """


if __name__ == "__main__":
    from sys import argv
    from urllib import error, request

    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
