# 0-simple_web_stack
+ [Diagram link:](https://photos.google.com/share/AF1QipN-bbX-qlhp_ctUvHicIxB8vgKlSY8YqrkLmj_YIlhMToI_ckdtttMHgGY-FMaq0g?key=anJJU2plNzRGMFRJVVZGSnNqOTZkeFpJcENxSGhn)  
  https://photos.google.com/share/AF1QipN-bbX-qlhp_ctUvHicIxB8vgKlSY8YqrkLmj_YIlhMToI_ckdtttM\HgGY-FMaq0g?key=anJJU2plNzRGMFRJVVZGSnNqOTZkeFpJcENxSGhn

## single server with a LAMP stack
+ 1 server
+ 1 web server (Nginx)
+ 1 application server
+ 1 application files (your code base)
+ 1 database (MySQL)
+ 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## Questions and Answers
+ What is a server  
  A server usually designed in "Server-Client" mode.  
  server process requests and deliver data to another computer over the internet  
  or a local network.  
+ What is the role of the domain name  
  Domain Name is a key in the dictionary, DNS server translate or map the domain name  
  to the ip address.
+ What type of DNS record www is in www.foobar.com  
  in DNS record, the type is CNAME  
+ What is the role of the web server  
  web server returns the webpages upon the client request from the web browser.  
+ What is the role of the application server  
  Apllication server is API between data server and client user, it takes user  
  request and access the data server, get the data that user need, rendering  
  webpages then return back to user.  
+ What is the role of the database  
  are used to store and manage databases and to provide data access for authorised users.
+ What is the server using to communicate with the computer of the user requesting the website  
  Web server

## Analysis and Conclusion:
   Simple web stack, this kind of web stack infrastructure, it is cost enconomically, 
   but for reliability consideration, it is not a good system design model. it has its  
   pittfalls. 1. SPOF, stand for Single Point Of Failure, any part inside the system  
   is breakdown, the whole system will crash.  
   2. Downtime When Maintenance needed. because no backup unit, when update needed,  
   have to shutdown the site, make the site not available for user.  
   3. Can not Scale: in case of high volumn of visitor, the site will slow down or  
   even worse going to crash.
