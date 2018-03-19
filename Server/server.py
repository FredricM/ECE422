import socket
import sys
import threading 
import os
import getpass
import collections
from os.path import isfile, join


class mdict(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)



def createHome(name, username):
    if not os.path.exists(username+"home"):
        os.makedirs(username+"home")
        print "created home directory for " + username

def addUser(name, sock, username, database):
    if username in database:
        sock.send( username +" already exists, please pick another name/")
        
    else:
        sock.send("input your password/")
        password = sock.recv(256)
        database[username] = password
        createHome("name", username)
        sock.send( username +" has been created/"+ directory)
        print database

def createFile(name, sock, filename):
    item = os.path.abspath(directory)
    completeName = os.path.join(item, filename+".txt") 
    if os.path.isfile(completeName):
    
        print(item)
        sock.send("already exists/" + directory)
       
    
    else:
        new_file = open(completeName, "w")
        new_file.close()
        sock.send("file created/" + directory)


       
def createGroup(name, sock, groupName, groupbase):
    if groupName in groupbase:
        sock.send("this group already exists/")
        
    else:
        groupbase[groupName]="root"
        sock.send("successfully created new group/")
        print groupbase
    

def addToGroup(name, sock, group, groupbase, database ):
    if group not in groupbase:
        sock.send("group doesn't exist/")

    else:
        sock.send("enter member")
        member = sock.recv(256)
        if member not in database:
            sock.send("user doesn't exist/")
        elif member in groupbase[group]:
            sock.send("user already in group/")
        else: 
            groupbase[group] = (member)
            sock.send("member added to the group/")
            print groupbase[group]
        
    
    return True

def login(name, sock, username, database):
    global user
    global directory
    if username not in database:
        sock.send("user doesn't exist/")
    else:
        sock.send("enter password: /")
        password = sock.recv(256)
        if database[username] == password:
            user = username
            directory = user+"home"
            sock.send("welcome " + user + "/" + directory)

       
            
        else:
            sock.send("incorrect password/")

def logout(name, sock):
    global user
    global directory
    sock.send("goodbye " + user + "/")
    user = ""
    directory = ""
    




database = {"root" : "ece492"}
groupbase = mdict()
user = ""
directory = ""


def server_program():

    # Create a TCP/IP socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket = socket.socket()
    # Bind the socket to the port
    server_address = ('localhost', 10008)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
       

        elif data[:3] == "add" and len(user) == 0:
            addUser("name", conn, data[4:], database)
    
        elif data[:6] == "create" and len(user) != 0:
            createFile("name", conn, data[7:])

        elif data[:6] == "newgrp" and len(user) == 0:
            createGroup("name", conn, data[7:] , groupbase)
            
        elif data[:6] == "memadd" and len(user) == 0:
            addToGroup("name", conn, data[7:], groupbase, database)
        
        elif data[:5] == "login" and len(user) == 0:
            login("name", conn, data[6:], database)
            print(user + "+" + directory)
            
        elif data[:6] == "logout" and len(user) != 0:
            logout("name", conn)

        else: 
            server_message = "not a command you can do/" + directory
            conn.send(server_message.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()


