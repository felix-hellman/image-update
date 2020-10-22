FROM python:alpine3.7
COPY . /drone
WORKDIR /drone
RUN pip install -r requirements.txt

