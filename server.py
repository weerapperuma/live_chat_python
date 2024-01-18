import socket
import threading
from tkinter import *

class ServerForm:
    def __init__(self):
        self.root = Tk()
        self.root.title("Server Form")

        self.btn_send = Button(self.root, text="Send", command=self.send_message)
        self.btn_send.pack()

        self.txt_input_field = Entry(self.root)
        self.txt_input_field.pack()

        self.txt_text_area = Text(self.root)
        self.txt_text_area.pack()

        self.data_input_stream = None
        self.data_output_stream = None
        self.server_socket = None
        self.local_socket = None
        self.message = ""

        threading.Thread(target=self.initialize_server).start()

        self.root.mainloop()

    def initialize_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(('localhost', 3012))
            self.server_socket.listen(1)

            self.txt_text_area.insert(END, "Server is Started !\n")

            self.local_socket, _ = self.server_socket.accept()
            self.txt_text_area.insert(END, "Client Connected !\n")

            self.data_input_stream = self.local_socket.makefile('rb')
            self.data_output_stream = self.local_socket.makefile('wb')

            while not self.message == "exit":
                self.message = self.data_input_stream.readline().strip().decode('utf-8')  # read Client's Msg
                self.txt_text_area.insert(END, f"Client: {self.message}\n")

        except Exception as e:
            print(e)
        finally:
            self.close_server()

    def send_message(self):
        if self.data_output_stream:
            message = self.txt_input_field.get().strip()
            self.data_output_stream.write((message + '\n').encode('utf-8'))
            self.data_output_stream.flush()
            self.txt_input_field.delete(0, END)

    def close_server(self):
        if self.local_socket:
            self.local_socket.close()
        if self.server_socket:
            self.server_socket.close()
        if self.data_input_stream:
            self.data_input_stream.close()
        if self.data_output_stream:
            self.data_output_stream.close()

if __name__ == "__main__":
    ServerForm()
