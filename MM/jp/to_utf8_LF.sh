#!/bin/bash
# Requires nkf (epel)
# Convert text files of "*.txt" to encoding in utf-8 and LF
find . -name "*.txt" -print0 | xargs -0 nkf -w --overwrite
find . -name "*.txt" -print0 | xargs -0 nkf -d --overwrite
