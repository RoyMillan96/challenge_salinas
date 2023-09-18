FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /codeDjango
COPY requirements.txt /codeDjango/
RUN pip install -r requirements.txt
COPY . /codeDjango/