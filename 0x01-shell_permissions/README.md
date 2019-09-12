su user = temporarily become he superuser
whoami = will indicate the username that I have and I am using in the system 
groups = shows us all the groups of which the current user is part
chown = we can change the owner of a file
touch = create an empty file
chmod = modify file access rights
chmod u+x,g+x,o+r = adds execute permission to the owner and the group owner, and read permission to other users
chmod ugo+x = add execution permission to the owner, the group owner and the other users, to the file
chmod 007 = set all permissions for other users only
chmod 753 = set all permissions for the user, write and execute for groups and write and execute for others
chmod --reference = Change the owner of a file, taking as reference the owner of another
chmod ugo+x = add execution permission to all subdirectories of the current directory for the owner, group owner and all other users
mkdir --mode=751 = create a directory with 751 permissions in the working directory.
chgrp = change group
chown -R = change the owner and group owner recursively
chown -h = change the owner and the owner of the file group of a symbolic link
chown --from = change the owner of the file only if it is owned by another user
telnet towel.blinkenlights.nl = for see star wars
