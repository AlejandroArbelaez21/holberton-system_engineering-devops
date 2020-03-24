#create a file in /tmp with puppet
file {'~/.ssh/ssh_config':
        ensure  => 'present',
        content => 'IdentityFile ~/.ssh/holberton',
}
file {'~/.ssh/ssh_config':
        ensure  => 'present',
        content => 'PasswordAuthentication no',
}

