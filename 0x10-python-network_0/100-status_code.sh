#!/bin/bash
# Doc
curl -s -o /dev/null -w "%{http_code}" "$1"
