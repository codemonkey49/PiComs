#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Boot
git pull origin master
sudo python Run.py
cd /

