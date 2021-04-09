FROM python:3.8

COPY requirements.txt .

RUN apt update
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

CMD python main.py