#In this web stack debugging task, we are testing how well our web server setup featuring Nginx 
#For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry
exec {'Sky_is_the_limit':
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
}
