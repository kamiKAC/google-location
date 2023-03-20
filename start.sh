#!/bin/sh
if [ -z $GOOGLE_EMAIL ]; then
    echo "Google email is required as GOOGLE_EMAIL env variable"
    exit 0;
fi
export MQTT_HOST="${MQTT_HOST:-`/sbin/ip route|awk '/default/{print $3}'`}"
export PYTHONUNBUFFERED=1
exec python3 google_location.py
