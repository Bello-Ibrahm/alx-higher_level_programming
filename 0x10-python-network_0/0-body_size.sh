#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

[ "$#" -eq 1 ] && curl -s "$1" | wc -c || echo "Usage: <./script>  <URL>"
