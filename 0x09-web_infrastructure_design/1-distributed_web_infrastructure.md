# 1-distributed_web_infrastructure
+ [Diagram link:](https://photos.google.com/share/AF1QipObkIZF99Nx_-_VioBL_DwCmjEOBC9BrJz_u6l9H7gtYkcsmGSzDlpO9VtWwUItHg?key=dkMwa0hoNHIwa1dXdzl6OWVVUmNZdUwybmxWUDJ3)
  https://photos.google.com/share/AF1QipObkIZF99Nx_-_VioBL_DwCmjEOBC9BrJz_u6l9H7gtYkcsmGSzDlpO9VtWwUItHg?key=dkMwa0hoNHIwa1dXdzl6OWVVUmNZdUwybmxWUDJ3

## Two servers with a LAMP stack
+ 2 servers
+ 1 web server (Nginx)
+ 1 application server
+ 1 load-balancer (HAproxy)
+ 1 set of application files (your code base)
+ 1 database (MySQL)

## Questions and Answers
+ For every additional element, why you are adding it?  
  we add one more sever to make whole system has backup, avoid SPOF.  
  we add load balancer to distributes traffic volumn to each sever, make the system  
  more reliable.
  we add set of application files, the make the site provides more services to users.  
+ What distribution algorithm your load balancer is configured with and how it works  
  The load balancing algorithm that is used determines which server, in a backend,   
  will be selected when load balancing.  
  RoundRobin is HAProxy default algorithm. it selects servers in turns.
+ Is your load-balancer enabling an Active-Active or Active-Passive setup,  
  explain the difference between both  
  HA for High Availability. HAProxy setup is make an infrastructure without a single point of failure.
  I prefer active/passive mode setup load balancer. add a health check to each balancer,  
  in case the primary node fail, floating IP will assign to secondary node.  
  Active-Active mode doest use floating IP, each load balancer only point to signle server,  
  it is traffic efficiency, but can't avoid the problem two balancer fail at the same time.
+ How a database Primary-Replica (Master-Slave) cluster works  
  database designed in Master/Slave mode to ensure consistency between redundant resources,  
  such as software or hardware components, to improve reliability, fault-tolerance, or accessibility.  
  the master database is regarded as the authoritative source, the slave databases are synchronized to it.
+ What is the difference between the Primary node and the Replica node in regard to the application  
  Primary node is selected active node to work to, the Replica node is passive node, backup in case fail  
  of primary node.

## Analysis and Conclusion:  
   Now the Web Stack Infrastructure have two servers. it solves SPOF problem.  
   also avoid Downtime when maintenance needed.  
   the system add Load Balancer, it distributes traffic volumn make it even to each server.  
   But this system don't have Firewall and HTTPS proxy, it has security issues potential.    
