import socket

import socket

QUEUE_SIZE = 5


def server():
    serv = socket.socket( 
               socket.AF_INET,
               socket.SOCK_STREAM)
    serv.bind(('', 5000))
    serv.listen(QUEUE_SIZE)

    # always listen for connections
    while True:
        conn, addr = serv.accept()
        print(f'Cntn: {addr}')
        from_client = ''

	    # Always listen for data
        while True:
            data = conn.recv(4096)

			# end of data
            if not data:
                break

            from_client += data.decode()
            print(from_client)
            conn.send("Server connection".encode())

        conn.close()
        print('client disconnected')


if __name__ == '__main__':
    server()
