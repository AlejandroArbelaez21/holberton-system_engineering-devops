#change the wrong number of request
exec {'change request number':
  provider => shell,
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
}
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
