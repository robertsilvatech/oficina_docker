FROM ubuntu:22.04

RUN apt update -y && \
    apt install -y python3.10 python3-pip

WORKDIR /app
COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY oficinadocker.py .
COPY templates/ templates/

VOLUME /data/logs/

ENV LOGFILE=/data/logs/example.log

EXPOSE 5000/tcp