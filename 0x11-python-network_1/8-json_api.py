#!/usr/bin/python3
""" Script that  takes in a letter and sends a POST reques
to http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    try:
        req = requests.post(url, data=payload)
        res = req.json()
        if not res:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
