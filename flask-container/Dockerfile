FROM python:3.8.13-alpine3.16
EXPOSE 80/tcp
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY static/ .
COPY templates .
COPY API_key.json .
COPY app.py .
COPY Functions.py .
COPY Response.py .