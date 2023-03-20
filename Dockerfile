FROM python:3.9-alpine3.17

RUN pip3 install locationsharinglib paho-mqtt
WORKDIR /glocation

COPY google_location.py start.sh ./
RUN mkdir -p /files \
    && chmod +x start.sh

CMD ./start.sh