FROM ubuntu:22.04

RUN apt update -y && \
    apt install -y python3.10 python3-pip

# Antes do Workdir
#COPY --chmod=777 example.sh /example/example.sh

WORKDIR /example
# Depois do Workdir
COPY --chmod=777 example.sh test/example.sh

ADD https://gist.githubusercontent.com/robertsilvatech/1449cf53f0cecb50ac92b503165696e6/raw/0f50117d360b08afb3e0beda19e119de2863d7e6/add-example.txt test/add-example.txt

ENV END_FOR=2