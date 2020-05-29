#change the wrong number
exec {'change_number_of_request':
  provider => shell,
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
}
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
