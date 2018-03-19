import socket
import sys


def client_program():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10008)
    # print >>sys.stderr, 'connecting to %s port %s' % server_address
    client_socket.connect(server_address)

    message = raw_input("//")  # take input
    directory = ""
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        if data.find("/") != None :
            directory = data[data.find("/"):]

            print('Received from server: ' + data[:data.find("/")])  # show in terminal

        message = raw_input(directory+"/")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
