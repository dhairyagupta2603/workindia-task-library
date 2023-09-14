FROM python:3.11-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /proj_server

COPY requirements.txt /proj_server/
RUN pip3 install -r requirements.txt

COPY . /proj_server/