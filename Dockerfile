FROM python:3.9.13-alpine3.16
RUN apk add make
RUN apk add libpq-dev
RUN apk add libffi-dev
RUN apk add python3-dev
RUN apk add build-base
WORKDIR /parking/server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD make run
