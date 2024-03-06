FROM python:3.8-slim-buster
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "rec_mon.py"]
