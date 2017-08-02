FROM tiangolo/uwsgi-nginx:python2.7

MAINTAINER Nick Lozon <nick.lozon@cleverfew.co>

RUN pip install flask

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY app /app
