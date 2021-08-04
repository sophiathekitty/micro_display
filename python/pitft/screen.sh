#!/bin/bash
echo "-----------------------------------"
echo "waiting to start (2 minutes)"
echo "-----------------------------------"
sleep 2m
while true; do
    echo "-----------------------------------"
    echo "starting python script"
    echo "-----------------------------------"
    sudo python3 /var/www/html/python/pitft/screen.py & > /home/pi/screenpy.log
    wait $!
    echo "-----------------------------------"
    echo "python script crashed (waiting)"
    echo "-----------------------------------"
    sleep 5m
    echo "-----------------------------------"
    echo "ready to restart"
    echo "-----------------------------------"
done
exit
