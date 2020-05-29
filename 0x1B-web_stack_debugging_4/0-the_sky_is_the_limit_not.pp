#In this web stack debugging task, we are testing how well our web server setup featuring Nginx 

exec {'sky is the limit':
  provider => shell,
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
}

exec {'restart ngnix':
  provider => shell,
  command  => 'sudo service nginx restart',
}
