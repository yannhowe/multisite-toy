FROM python:3.7-buster
RUN apt update && apt install -y libmariadbclient-dev
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
COPY . /usr/src/app/