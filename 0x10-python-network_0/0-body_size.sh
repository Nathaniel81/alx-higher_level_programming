#!/bin/bash
# Doc

curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
