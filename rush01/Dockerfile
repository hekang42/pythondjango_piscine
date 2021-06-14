FROM python:3.9.5-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pillow
RUN pip install -r requirements.txt

COPY . .
