FROM continuumio/miniconda3

LABEL maintainer="shihao1007@gmail.com"

RUN conda install -y -c conda-forge pandas nltk plotly dash

RUN apt-get update

RUN apt-get install -y sqlite3 libsqlite3-dev

VOLUME '/app'

EXPOSE 80

CMD python /app/app.py