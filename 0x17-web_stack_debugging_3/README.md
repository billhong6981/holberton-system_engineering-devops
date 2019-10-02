# Project: 0x17. Web stack debugging #3

## Learning Objectives:
+ curl -sI 127.0.0.1 get 500 status code (blame on server side)
+ pstree -a && netstat -lpnt (apache2 service is on)
+ install tmux multi terminale, tmux open session, ctrl + b c open 2 windows
+ pstree -a (to get apache2 www-html pid is 88)
+ strace -p 88 (attach pid 88 on one window)
+ switch to another window, run: curl -sI 127.0.0.1
+ get "/var/www/html/wp-includes/class-wp-locale.phpp" file not exist
+ got to copy /var/www/html/wp-includes/class-wp-locale.php to
+ "/var/www/html/wp-includes/class-wp-locale.phpp"
+ curl -sI 127.0.0.1 now got 200 status code OK
