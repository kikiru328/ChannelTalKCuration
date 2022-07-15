FROM python:3.9.13-alpine

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY ./static .
COPY ./templates .
COPY Functions.py .
COPY Response.py . 