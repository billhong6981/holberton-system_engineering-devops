# Automated by Puppet manifest to install web server nginx
# and reconfiguration
exec { 'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}
-> file_line { 'Add redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4;',
}
-> file_line { 'Add custom HTTP server':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By ${hostname};',
}
-> file { '/var/www/html/index.html':
  content => 'Holberton School',
}
-> service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
