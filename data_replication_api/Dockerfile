# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /data_replication_api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run"]