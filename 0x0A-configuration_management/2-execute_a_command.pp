# using puppet manifest file to kill process
exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
