FROM ubuntu:xenial

MAINTAINER Nick Lozon <nick.lozon@cleverfew.co>

RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install nose2 flask

COPY . /app

WORKDIR /app

ENTRYPOINT [ "bash", "tests/runtests.sh" ]
