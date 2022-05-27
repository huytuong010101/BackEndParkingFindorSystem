FROM python:3.9.13-alpine3.16
RUN apk add make
WORKDIR /parking/server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN make init-db
CMD make run