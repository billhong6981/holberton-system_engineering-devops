# puppet manifest file that modifies client configuration file
# so that login server using key authentication and no password asked
file_line { 'No_password':
  path  => '/etc/ssh/ssh_config',
  line  => '\tPasswordAuthentication no',
  match => '\s*PasswordAuthentication yes',
}

file_line { 'Key_file':
  path  => '/etc/ssh/ssh_config',
  line  => '\tIdentityFile ~/.ssh/holberton',
  match => '\s*IdentityFile **',
}
