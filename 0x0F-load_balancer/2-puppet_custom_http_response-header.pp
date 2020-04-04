#This script containg commands to automatically configure an Ubuntu machine to respect above requirements
exec { 'install_nginx_puppet':
  command  => "sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i '/listen 80 default_server;/a\\\tadd_header X-Served-By $HOSTNAME;' /etc/nginx/sites-enabled/default && sudo service nginx restart",
  provider => "shell",
}
