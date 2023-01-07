FROM python:3-slim-buster

WORKDIR /fastapi_database_demo

ADD . /fastapi_database_demo

COPY requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]