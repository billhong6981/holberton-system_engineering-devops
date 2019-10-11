# puppet manifest to automate changing ULIMIT size of open files in nginx

exec { 'changeMe':
  path    => ['/bin/'],
  command => 'sed -i "s/-n 15/-n 1000/" /etc/default/nginx',
  notify  => Service['nginx']
}

service { 'nginx':
  ensure => running,
  enable => true
}
