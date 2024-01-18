import socket
import threading
HOST = '192.168.56.1'
PORT = 9999

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((HOST,PORT))
        print(f"Successfully connected to the server {HOST}:{PORT}")
    except:
        print(f"Unable to connect to server {HOST} {PORT}")


if __name__ == '__main__':
    main()