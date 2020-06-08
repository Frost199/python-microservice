# python-microservice
A Simple Hotel service, using a microservice running on nameko

The idea of a microservice is to not have a monolith solution as always proposed.

The concept of having individual services which are losely coupled makes you think of your application as a plug and detach system  
It is often regarded to have **"smart endpoints  but dumb pipelines"**

In other words, an application following a microservices architecture is composed of several independent and dynamic services that communicate  
with each other using a communication protocol. 

It is common to use HTTP (and REST), but as we see in this project, we can use other types of communication protocols such as  
**RPC (Remote Procedure Call) over AMQP (Advanced Message Queuing Protocol)**.

## Running
```
docker-compose up
``` 

The microservices are broken up into two
* Rooms service
* Bookings service


Ideally, you would want each service to have its own databases and communication between each service  
should be done over a **_publisher-subscriber pattern_** or have another microservice that helps with the communication  
between other microservice, this can be best seen when working with authentication wth **_JWT_** tokens

In our tutorial, we tried not to make things complicated and used a single database for communication, but ideally, they should have their own individual database.  

If you notice you are constantly updating two or more microservices at a given time, that  
is a sign that those microservices share a lot in common and they should be integrated into one microservice

[A very good discussion by Martin fowler on microservices.](https://martinfowler.com/articles/microservices.html)
