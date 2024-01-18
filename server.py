import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTNER_LIMIT =5
def main():

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        server.bind((HOST,PORT))
    except:
        print(f"Unable to Bind to host{HOST} and port {PORT}")


    #set server limit
    server.listen(LISTNER_LIMIT)

    while 1:
        client,address = server.accept()
        print(f"Successfully connected to a client {address[0]} {address[1]}")


if __name__ =='__main__':
    main()

