# kill the process named killmenow
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/Holberton/holberton-system_engineering-devops/0x0A-configuration_management',
}
