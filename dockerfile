FROM python:3.12.1-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["bash", "runtime.sh"]