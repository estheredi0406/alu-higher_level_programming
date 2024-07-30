#!/bin/bash
#This script actually takes in a URL, sends a request and displays the size of the body of the response
curl -sw "$1" | grep "Content-Length" | cut -d " " -f2
