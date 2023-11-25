# google-location
This Python script fetches the location data from Google and publishes it to MQTT.


This script has been provided by user Marmoset_Threat in [this thread](https://community.openhab.org/t/google-family-location-sharing-in-openhab-via-python-and-mqtt/) on openHAB community forum 

I've adopted script for use in Docker container.

# Using with Docker

Folowing env variables can be passed to Docker container to configure it:
<ul>
<li>GOOGLE_EMAIL - email to log in to Google services (empty by default, required)
<li>COOKIES_FILE - file with session cookies (default 'googlemaps_cookie.txt')
<li>MQTT_CLIENT_NAME - name of the MQTTclient (default 'google_location_mqtt')
<li>MQTT_HOST - hostname or ip address of MQTT server (default 'localhost')
<li>MQTT_PORT - port of MQTT server (default '1883')
<li>MQTT_TOPIC - topic to which events will be stored to (default 'googlelocation/')
<li>MQTT_USER - username for MQTT authentication (empty by default)
<li>MQTT_PASS - password for MQTT authentication (empty by default)
<li>INTERVAL - Google location services polling interval in seconds (default 60)
</ul>

Example usage:

    put your googlemaps_cookie.txt in current directory
    docker run -ti --name google-location -e GOOGLE_EMAIL=my_email@gmail.com -v ./:/files/ kamikac/google-location


