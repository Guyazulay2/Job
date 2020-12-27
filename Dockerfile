FROM ubuntu:latest


ENV VERSION=1.2.0

RUN apt update \
    && apt-get upgrade -y \
    && apt-get install python3 -y \
    && apt-get install vim -y \
    && apt-get install zip unzip -y

COPY zip_job.py /tmp

ENTRYPOINT [ "ls", "/tmp" ]
