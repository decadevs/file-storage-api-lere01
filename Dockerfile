# Docker File

# Base image
FROM python:3

# Author
LABEL version = "Faith O. Oyedemi"

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Work directory
ADD . /app
WORKDIR /app

# Dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# final command
# CMD python manage.py runserver 0.0.0.0:8000

