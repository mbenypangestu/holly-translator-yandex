#!/bin/bash
git add .
git commit -m "Update"
git pull origin master
ps aux | grep 'main.py' | grep -v grep | awk '{print $2}' | xargs kill
nohup python3 main.py &
