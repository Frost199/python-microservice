# setup the python version alphine means a lightweight
FROM python:3.7-alpine

# maintainer
MAINTAINER Eleam Emmanuel

# run a system update
RUN apt-get update && apt-get -y install netcat && apt-get clean

# make our app directory, switch to the app dir and
# make it our working directory and copy ./app to /app
RUN mkdir /app
WORKDIR /app

# run python in an unbuffered mode
ENV PYTHONUNBUFFERED 1

# copy requirements.txt and run pip install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy config, run.sh and hotel-gateway
COPY config.yml ./
COPY run.sh ./
COPY bookings-gateway.py ./

# create a user that will run the application using docker
RUN adduser -D manny
USER manny

# Give run.sh permissions and run it
RUN chmod +x ./run.sh
CMD ["./run.sh"]
