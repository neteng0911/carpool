# Pull base image
FROM python:3.10
#FROM ubuntu:22.04
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/
#RUN apt-get update
#RUN apt-get install -y python3
#RUN apt-get install -y python3-pip
RUN pip install --upgrade pip

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#ENTRYPOINT ["python3"]
#CMD ["python3"]
# Copy project
COPY . .