#create a file in /tmp with puppet
file_line {'Declare identity file':
        path    => '/home/alejandro/.ssh/ssh_config',
        line    => "IdentityFile ~/.ssh/holberton\n",
}

file_line {'Turn off passwd auth':
        path    => '/home/alejandro/.ssh/ssh_config',
        line    => "IdentityFile ~/.ssh/holberton\n",
}

