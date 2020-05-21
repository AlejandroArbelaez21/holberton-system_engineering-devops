#Using strace, find out why Apache is returning a 500 error
#use tmux to run strace in one window and curl in another one
exec {'strace_is_my_friend':
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
