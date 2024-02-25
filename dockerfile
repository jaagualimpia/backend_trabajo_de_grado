FROM python:3.10-alpine

RUN apk update && apk add bash

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["bash", "runtime.sh"]