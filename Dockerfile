FROM python:3.11-alpine

RUN pip3 install locationsharinglib paho-mqtt
WORKDIR /glocation

COPY google_location.py start.sh ./
RUN mkdir -p /files \
    && chmod +x start.sh

CMD ./start.sh