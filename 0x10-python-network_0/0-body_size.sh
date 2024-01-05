#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" -eq 0 ]; then
	echo "Usage: <./script_name> <www.example.com:port>"
else
	curl -s "$1" | wc -c
fi
