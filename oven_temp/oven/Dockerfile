FROM python:3.9

WORKDIR /app

COPY ./app /app

EXPOSE 80

RUN pip install --no-cache-dir --upgrade pip setuptools

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
