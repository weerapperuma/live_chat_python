import socket
import threading
import tkinter as tk
from tkinter import ttk

HOST = '192.168.56.1'
PORT = 9999
LISTENER_LIMIT = 5
server_running = False
status_var = None

def start_server():
    global server_running
    server_running = True

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
    except:
        print(f"Unable to Bind to host {HOST} and port {PORT}")
        server_running = False
        return

    server.listen(LISTENER_LIMIT)
    while server_running:
        client, address = server.accept()
        print(f"Successfully connected to a client {address[0]} {address[1]}")

    server.close()

def create_ui():
    global status_var
    root = tk.Tk()
    root.title("Server Status")

    label = ttk.Label(root, text="Server Status:")
    label.grid(row=0, column=0, padx=10, pady=10)

    status_var = tk.StringVar()
    status_var.set("Server not started")

    status_label = ttk.Label(root, textvariable=status_var)
    status_label.grid(row=0, column=1, padx=10, pady=10)

    start_button = ttk.Button(root, text="Start Server", command=start_server_thread)
    start_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

def start_server_thread():
    if not server_running:
        server_thread = threading.Thread(target=start_server)
        server_thread.start()
        status_var.set("Server running on {}:{} with a listener limit of {}".format(HOST, PORT, LISTENER_LIMIT))

if __name__ == '__main__':
    create_ui()
