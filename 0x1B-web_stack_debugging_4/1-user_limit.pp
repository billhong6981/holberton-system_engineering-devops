# puppet manifest to automate change /etc/security/limits.conf open files limit

exec { 'change-os-configuration-for-holberton-user':
  path    => ['/bin/'],
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1024/" \
  /etc/security/limits.conf'
}

exec { 'change-os-configuration-for-holberton-user1':
  path    => ['/bin/'],
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" \
  /etc/security/limits.conf'
}
