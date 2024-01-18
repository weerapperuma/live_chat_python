import socket
import threading
from tkinter import *

class ClientForm:
    def __init__(self):
        self.root = Tk()
        self.root.title("Client Form")

        self.btn_send = Button(self.root, text="Send", command=self.send_message)
        self.btn_send.pack()

        self.txt_input_field = Entry(self.root)
        self.txt_input_field.pack()

        self.txt_text_area = Text(self.root)
        self.txt_text_area.pack()

        self.data_input_stream = None
        self.data_output_stream = None
        self.remote_socket = None
        self.message = ""

        threading.Thread(target=self.initialize_client).start()

        self.root.mainloop()

    def initialize_client(self):
        try:
            self.remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.remote_socket.connect(('192.168.56.1', 3012))

            self.data_output_stream = self.remote_socket.makefile('wb')
            self.data_input_stream = self.remote_socket.makefile('rb')

            while not self.message == "exit":
                self.message = self.data_input_stream.readline().strip().decode('utf-8')
                self.txt_text_area.insert(END, f"Server: {self.message}\n")

        except Exception as e:
            print(e)
        finally:
            self.close_client()

    def send_message(self):
        if self.data_output_stream:
            message = self.txt_input_field.get().strip()
            self.data_output_stream.write((message + '\n').encode('utf-8'))
            self.data_output_stream.flush()
            self.txt_input_field.delete(0, END)

    def close_client(self):
        if self.remote_socket:
            self.remote_socket.close()
        if self.data_input_stream:
            self.data_input_stream.close()
        if self.data_output_stream:
            self.data_output_stream.close()

if __name__ == "__main__":
    ClientForm()
