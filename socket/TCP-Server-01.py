import socket
import contextlib

def main():
    host = "127.0.0.1" # localhost
    port = 4321
    backlog = 10
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with contextlib.closing(sock):

        sock.bind((host, port))
        sock.listen(backlog)

        while True:
            conn, address = sock.accept()

            with contextlib.closing(conn):
                msg = conn.recv(bufsize)
                msg_decode = msg.decode() # byte → str
                print(msg_decode)
                conn.send(msg)


    return




if __name__ == "__main__":
    main()

