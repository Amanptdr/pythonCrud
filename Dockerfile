FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 7000

WORKDIR /usr/src/django_app
COPY projectShop/requirements.txt .
RUN python -m pip install --upgrade pip
# RUN mkdir /var/log/mypythonBackend
RUN apt update && \
    pip install --no-cache-dir -r requirements.txt

# pip install setuptools==57.4.0 && \
# RUN apt-get -y install cron