# 3-scale_up
+ [Diagram link:](https://photos.google.com/share/AF1QipMD4ZOTug2C3u2Qvk8iNMxSVHecLhFHpXLrizkCxGl1E1bs71qLaLy0c8Xtokg0qA?key=aTJCaVBWTGtqbnRPTmdpYzBvM3lzNkpGdWpBRGV3)
  https://photos.google.com/share/AF1QipMD4ZOTug2C3u2Qvk8iNMxSVHecLhFHpXLrizkCxGl1E1bs71qLaLy0c8Xtokg0qA?key=aTJCaVBWTGtqbnRPTmdpYzBvM3lzNkpGdWpBRGV3


## Three servers with a LAMP stack
(current project add one server to be HAProxy server)
+ 1 server  
  1 load-balancer (HAproxy) configured as cluster with the other one  
  Split components (web server, application server, database) with their own server  

(below is previous web stack infrastructure)
+ 2 servers  
  1 web server (Nginx)  
  1 application server  
  1 set of application files (your code base)  
  1 database (MySQL)  

+ 3 firewalls  
  1 SSL certificate to serve www.foobar.com over HTTPS  
  3 monitoring clients (data collector for Sumologic or other monitoring services)  

## Questions and Answers  
+ why we add 1 server fullfill Load Balancing job?  
  the sever will use layer 7 reverse proxing, load balancing.  
  Configure HAProxy setting to make the website with a single domain name that serves  
  multiple applications such as(Web server, Data server, Application server)  
  as the http requests can be analyzed to decide which application should receive  
  the traffic. the system will increases reliability, 
  security, speed also get improve.

## Analysis and Conclusion:  
   This Web Stack Infrastructure have: one domain name, one server in the front entrance  
   setting with HAProxy, layer 7 reverse proxing, load balancing setting to distributes  
   the workflow, direct the connection to specified server upon the user request. also  
   set up the firewall for the site security purpose. install the SSL certificate  
   to use the 443 port to transport informations. two Servers backup each other to make  
   system redundancy, avoid the downtime problem and single point on failure(SPOF)  
   each server set up with Web Server, Application Server, Database, code base for managerment  
   the website. Database storage setup with one storage is master mode, one is slave which  
   update/sychronize from the master. each server set up firewall, and run the monitoring  
   tool all the time to measure the performance of the site.
