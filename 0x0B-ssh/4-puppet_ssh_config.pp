# puppet manifest file that modifies client configuration file
# so that login server using key authentication and no password asked
file_line { 'No_password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
  match  => '\s*PasswordAuthentication yes',
}

file_line { 'Key_file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
  match  => '\s*IdentityFile **',
}
