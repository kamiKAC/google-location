FROM python:3.11-alpine

RUN apk update && apk upgrade --no-cache \
    && apk add --no-cache openssl openssl1.1-compat

RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir locationsharinglib paho-mqtt
    
WORKDIR /glocation
COPY google_location.py start.sh ./
RUN mkdir -p /files \
    && chmod +x start.sh

CMD ./start.sh
