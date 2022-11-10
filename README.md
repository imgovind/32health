# 32health


# Instructions to Run the API
- cd processor
- docker build -f DockerFile . -t 32health-backend-test
- docker run -it -p 8000:8000 32health-backend-test
- Import the provided postman collection and execute against the API
- If you have Sql Pro or any other similar DB, you can view the db table on sqlite3 


# Thoughts behind the API
1. I chose Django as the framework of choice because it comes ready to go with sqlite3 as its database right out of the box, I could have gone ahead with Fastapi, but I chose Django because of its boilerplate code generator as well. 
2. The conventions that Django has put out for developers to use are pretty straightforward, and I was quickly able to set up my models and serializer and perform data migrations.
3. I created routes that matched all the paths using regex for the claims endpoint. 
4. I later refactored the code to have a service layer that did all the business logic regarding the calculation of net fees and yanked out the deserializing using a custom helper function (a hack still), but I was quickly able to get the endpoint up and running.
5. Refactoring the code to use the service layer helped me unit-test the methods and test the validations presented in the instructions. 
6. I made three assumptions about using the API
7. Since CSV was given, I assumed there would be a bulk endpoint or a script to ingest the CSV file and make a bunch of API calls to ingest the claims. I chose the latter as the case since this could also be a timed operation running on a cron job or something similar.
8. I assumed that all the inputs would be a string and that the validation would happen in the API, making the script simpler, thereby preserving all logic with the API repo. 
9. I represented all the dollar amounts as cents in the database to simplify the calculations. 
10. The final decision I made with the API is that the downstream actions would be event-driven. The payments service will consume an event triggered by the POST endpoint. The trigger would be an asynchronous operation. This could run either on Kafka or RabbitMQ. (I've added this in the comments section in the events_service.py file. Earlier it was in views.py, but then I refactored a bit, haha; sorry for that!) 
11. Initially, there will be a main payments queue from which the payments service will consume the messages one by one. In the event of any failure on the payments service side, the message will be put into a failure queue. A cron job would later try shoveling messages from the failure queue to the main queue for reprocessing. 
12. This is where the metrics and monitoring would come in handy. We should have some metrics around the number of messages in the queue and the number of messages being acked (acknowledged) by the payments service. 
13. This could be the basis for elastic scaling based on these metrics. This would spin up more payment service nodes or wind them down based on the traffic. 
14. Likewise, some metrics around web traffic can help spin up more Django web instances or wind them down. 
15. One design choice I'd like to make here would be to have a cloud provider agnostic solution running this service in two cloud providers like AWS and GCP or on colocated servers. Using BGP for this and declaring two AS for discovery by the nameservers at the ISP level would ensure near 100% availability. I am not saying 100% availability because in the event DNS resolution collectively fails on multiple AS, the service would be down. 
16. All this finally boils down to the final single point of failure: the transactional database we are using as a backing store. I prefer to use Google's spanner database because it provides Consistency, Availability, and Partition tolerance all in one. This could be a quick solution to implement. Still, a truly robust solution would be to use multiple relational databases, consistent hashing, and a comprehensive hash ring that would allow us to partition data across multiple databases in a horizontal sharding fashion. We need to set up multiple copies of this hash ring and use a good consensus algorithm to keep them in sync. 
17. Finally, I initially used Pascal Casing but then moved to snake casing since that's what's preferred nowadays. I refactored the code to reflect this. 

