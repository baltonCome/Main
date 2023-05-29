FROM python:3.9
ENV PYTHONUNBUFFERED 1
COPY . /app/
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt-get install -y libpq-dev