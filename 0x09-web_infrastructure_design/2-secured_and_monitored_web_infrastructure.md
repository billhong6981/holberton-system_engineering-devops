# 2-secured_and_monitored_web_infrastructure
+ [Diagram link:](https://photos.google.com/share/AF1QipMM6LU2lLusMViX8ZjgZK33-P74I7Vg00HGbeZpT8q4qaEan0KmtT0_VkJQU6kOQw?key=aWlKb194VmgtSXpJUGtPS3lWWThwd1RsdG9JN0JR)
  https://photos.google.com/share/AF1QipMM6LU2lLusMViX8ZjgZK33-P74I7Vg00HGbeZpT8q4qaEan0KmtT0_VkJQU6kOQw?key=aWlKb194VmgtSXpJUGtPS3lWWThwd1RsdG9JN0JR

## Two servers with a LAMP stack
+ 3 firewalls
+ 1 SSL certificate to serve www.foobar.com over HTTPS
+ 3 monitoring clients (data collector for Sumologic or other monitoring services)

## Questions and Answers
+ For every additional element, why you are adding it
  Add FireWall to Load Balancer, because load balancer is the gateway between user and  
  server, set firewall in the frontie
  Add Firewall to each Server to protect it.
  Install SSL certificate to secure information between site and user. redirect HTTP  
  port to HTTPS port.
  Add three tools to monitor the performance of web app, web data, and web code.

+ Why is the traffic served over HTTPS
  A site served over HTTPS is more secure. Since https uses the secure port 443  
  which encrypts outgoing informations. Regular http use port 80, send infos via plain text.

+ What monitoring is used for
  Monitoring is a set of tool to use for measuring the performance of server running

+ How the monitoring tool is collecting data
  The moitoring tool evalue every unit in the infrastructure, consider which work metrics  
  and resource metrics are reasonably available, and collect them all.
+ Explain what to do if you want to monitor your web server QPS
  install the tool Sumologic to monitor the disk I/O, MySql, Memory, Network, CPU

## Analysis and Conclusion:  
+ Why terminating SSL at the load balancer level is an issue
    Load Balancer is locate in between internet and server, is the first entrance port  
    then set the port with 443 is more safe.
+ Why having only one MySQL server capable of accepting writes is an issue
    setting one MySql server in primary, ative all the time, the other data sever is Reblica,  
    only synchronized to the first sever, to ensure the data not to depart.
+ Why having servers with all the same components (database, web server and application server)  
might be a problem
