#create a file in /.ssh with puppet
file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/alejandro/.ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/alejandro/.ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}
