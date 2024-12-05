FROM python:3.8.5-alpine3.11

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

RUN pip install flask --upgrade

RUN pip install "jinja2<3.1"

ENTRYPOINT python app.py