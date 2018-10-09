
import socket


def server_client_program():
    # get the hostname
    host = socket.gethostname()
    port = 3111  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    #client socket
    port_client = 2999  # initiate port no above 1024
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port_client))  # connect to the server


    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if data:
            print("from connected user: " + str(data))
            # if data is received send that to port 2999
            client_socket.send(data.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_client_program()
