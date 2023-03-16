FROM ubuntu:22.04

RUN apt update -y && \
    apt install -y python3.10 python3-pip

WORKDIR /app
COPY logging-example.py .

VOLUME /data/logs/

ENV LOGFILE=/data/logs/example.log