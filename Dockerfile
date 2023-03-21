FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# make a directory in our Docker image in which we can use to store our source code
# Copy the project folder from our local machine to the docker image
RUN mkdir /project
WORKDIR /project

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]