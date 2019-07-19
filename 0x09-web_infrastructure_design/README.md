# Project: 0x09-web_infrastructure_design

## Learning Objectives
+ Able to draw a diagram covering the web stack that we built in project
+ Able to explain what each component is doing in the web stack
+ Able to explain system redundancy
+ Know all the mentioned acronyms: LAMP, SPOF, QPS

## Tasks
+ 0. Simple web stack: descripes about simple web infrastructure,a single server with a LAMP stack.

+ 1. Distributed web infrastructure:
  2 servers
  1 web server (Nginx)
  1 application server
  1 load-balancer (HAproxy)
  1 set of application files (your code base)
  1 database (MySQL)

+ 2. Secured and monitored web infrastructure
  3 firewalls
  1 SSL certificate to serve www.foobar.com over HTTPS
  3 monitoring clients (data collector for Sumologic or other monitoring services)

+ 3. Scale up
  1 server
  1 load-balancer (HAproxy) configured as cluster with the other one
  Split components (web server, application server, database) with their own server

# Author
+ Bill Huang
