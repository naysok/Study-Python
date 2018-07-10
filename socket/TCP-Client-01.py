import socket
import contextlib

def main():
    host = "127.0.0.1"
    port = 4321
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with contextlib.closing(sock):

        sock.connect((host, port))

        #sock.send(b"Hello World!!")
        str_tmp = input("please enter messange : ")
        str_input = bytes(str_tmp,'UTF-8') # str →　byte

        sock.send(str_input)

        print(sock.recv(bufsize))

    return

if __name__ == "__main__":
    main()
