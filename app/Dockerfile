FROM alpine:3.12.7

CMD ["python3"]

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN apk add -U --no-cache bash python3 python3-dev libpq postgresql-dev unixodbc-dev musl-dev g++ libffi-dev \
  py3-pip rust cargo docker-py \
  && pip3 install --upgrade --no-cache-dir pip setuptools \
  && pip3 install --no-cache-dir --ignore-installed six -r requirements.txt \
  && ln -s /usr/bin/python3 /usr/bin/python
#  && apk del --no-cache python3-dev postgresql-dev unixodbc-dev musl-dev g++ libffi-dev
