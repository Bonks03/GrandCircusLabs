FROM confluentinc/cp-kafka:7.3.0
FROM python:3.9


RUN apt-get update && \
    apt-get install -y python3-pip

COPY requirements.txt /app/

WORKDIR /app

COPY ./app/ /app

RUN pip install --no-cache-dir --upgrade pip setuptools

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
