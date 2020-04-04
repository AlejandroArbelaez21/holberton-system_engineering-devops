#This script containg commands to automatically configure an Ubuntu machine to respect above requirements
exec { 'custom_header_puppet':
  command  => "sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i '18i \\\tadd_header X-Served-By $hostname;' /etc/nginx/sites-enabled/default && sudo service nginx restart",
  provider => "shell",
}
