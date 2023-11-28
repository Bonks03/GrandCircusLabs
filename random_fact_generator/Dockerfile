FROM python:3.9

USER root

RUN apt-get update && \
    apt-get install -y python3-pip

COPY requirements.txt /app/

WORKDIR /app/

RUN pip3 install --no-cache-dir --upgrade pip setuptools

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
