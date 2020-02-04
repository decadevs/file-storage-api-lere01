# Docker File

# Base image
FROM python:3.6.1

# Author
LABEL version = "Faith O. Oyedemi"

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Work directory
ADD . /app
WORKDIR /app

# copy requirements file
# COPY 
# COPY requirements.txt ./
# COPY startup.sh ./
# COPY manage.py ./

# Dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# expose ports
EXPOSE 8100


# final command
# CMD ["./startup.sh"]
CMD python manage.py runserver 0.0.0.0:8100

