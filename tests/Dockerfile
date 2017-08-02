FROM tiangolo/uwsgi-nginx-flask:flask

MAINTAINER Nick Lozon <nick.lozon@cleverfew.co>

RUN pip install nose2 flask

COPY . /app

WORKDIR /app

ENTRYPOINT [ "bash", "runtests.sh" ]
