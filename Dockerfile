FROM python:3.10-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY science_famcs_back/ ./science_famcs_back/
COPY storage/ ./storage/
COPY authentication/ ./authentication/
COPY db.sqlite3 ./db.sqlite3
COPY manage.py ./manage.py
