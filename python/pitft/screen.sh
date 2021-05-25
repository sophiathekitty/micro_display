#!/bin/bash
sleep 2m
while true; do
    sudo python3 /var/www/html/python/pitft/screen.py &
    wait $!
    sleep 10
    echo "script crashed"
done
exit
