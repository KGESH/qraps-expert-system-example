FROM python:3.8

COPY . /app

RUN pip install requests
RUN pip3 install flask

WORKDIR /app

CMD ["python3", "./app.py"]
