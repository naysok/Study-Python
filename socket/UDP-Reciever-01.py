import socket
import contextlib

def main():

    host = "127.0.0.1"
    port = 4000
    bufsise = 4096

    reciver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with contextlib.closing(reciver_sock):

        reciver_sock.bind((host, port))

        while True:
            recv_msg = reciver_sock.recv(bufsise)
            recv_msg_decode = recv_msg.decode() # byte → str

            print(recv_msg_decode)

    return

if __name__ == "__main__":
    main()