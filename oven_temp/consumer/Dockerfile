FROM jupyter/pyspark-notebook

WORKDIR /app

COPY ./app/ /app

COPY jars/spark-streaming-kafka-0-10_2.12-3.3.2.jar /usr/local/spark/jars/
COPY jars/spark-sql-kafka-0-10_2.12-3.3.2.jar /usr/local/spark/jars/
COPY jars/kafka-clients-3.4.0.jar /usr/local/spark/jars/
COPY jars/spark-token-provider-kafka-0-10_2.12-3.3.2.jar /usr/local/spark/jars/
COPY jars/commons-pool2-2.11.1.jar /usr/local/spark/jars/

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]