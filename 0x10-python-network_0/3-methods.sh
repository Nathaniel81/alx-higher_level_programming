#!/bin/bash
# Doc
curl -sLiX OPTIONS "$1" | grep Allow | cut -d " " -f 2-
