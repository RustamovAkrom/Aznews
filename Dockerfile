FROM python:3.10.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /.

WORKDIR /.

COPY requirements.txt /./

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /./