#In this web stack debugging task, we are testing how well our web server setup featuring Nginx 
#For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry
exec {'sky_is_the_limit':
  provider => shell,
  command  => "sed -i 's/15/2000/g' /etc/default/nginx",
}

exec {'restart_ngnix':
  provider => shell,
  command  => 'sudo service nginx restart',
}
