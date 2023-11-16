FROM confluentinc/cp-zookeeper:latest

USER root

COPY requirements.txt /app/

FROM python:3.10

WORKDIR /app/

RUN pip install --no-cache-dir --upgrade pip setuptools
RUN apt-get update && \
    apt-get install -y python3-pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]