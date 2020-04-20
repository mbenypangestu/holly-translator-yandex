#!/bin/bash
cd ~/projects/holly-translator-yandex
git pull origin master
ps aux | grep 'main.py' | grep -v grep | awk '{print $2}' | xargs kill
nohup python3 main.py &
