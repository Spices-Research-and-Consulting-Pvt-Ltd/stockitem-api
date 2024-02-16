# Use an official Python runtime as the base image
FROM python:3.11-slim

RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential apache2
RUN apt-get install -y libapache2-mod-wsgi-py3

WORKDIR /app

COPY requirements.txt /app/
COPY app.conf /etc/apache2/sites-available/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /var/www/html/app/

RUN a2ensite app.conf
RUN a2dissite 000-default.conf
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_balancer
RUN a2enmod lbmethod_byrequests
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
