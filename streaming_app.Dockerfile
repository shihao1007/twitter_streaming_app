FROM continuumio/miniconda3

LABEL maintainer="shihao1007@gmail.com"

RUN conda install -y -c conda-forge pandas tweepy sqlalchemy sqlalchemy-utils urllib3

RUN apt-get update

RUN apt-get install -y sqlite3 libsqlite3-dev

RUN mkdir /app

RUN /usr/bin/sqlite3 /app/tweets.sqlite

EXPOSE 5050

CMD python /app/data_gathering/streaming.py