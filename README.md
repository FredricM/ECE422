# ECE422
project 1
Fredric Mendi 1410462

1.in directory with server.py & (Server directory)
python server.py 

2.in another terminal in directory with client.py:
python client.py


3.type in commands in the client terminal
  type: add "username" : this will add a username if not already in database, and prompt you for a password, creates a directory for you
  type: newgrp "groupname" : this will add a new group if not already existing. 
  type: memadd "groupname": this will check if group exists, prompts a member that exists to be added to this "groupname"
  type: login "username : this will ask for your password, if not correct need to type command and username
 
 once logged in (previous commands do not work):
  type: create "filename" : this will create a file in your directory.
  type: logout : this will log you out
  
 4.anytime in the client terminal
  type: bye : if you type bye at any time you shut down both client and server
  


Notes: (things not implemented but Mentioned in Design, check Design folder)
*server has not been set up with a online database. once server shutdowns, everything is reset, files/directories remain
*cannot modify(read, write, delete, rename) file 
*cannot login as a guest
*doesn't have ls command
*cannot create another directory
*no notification if another user has modified file.
*no encrpytion when a guest views files and directories.
*no permission flags on files and directories
