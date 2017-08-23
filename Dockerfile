FROM tiangolo/uwsgi-nginx-flask:python2.7

MAINTAINER Nick Lozon <nick.lozon@cleverfew.co>

COPY ./app /app
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
