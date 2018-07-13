import socket
import time
import contextlib

def main():

    host = "127.0.0.1"
    port = 4000
    count = 0

    sender_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with contextlib.closing(sender_sock):

        while True:
            msg = "Hello World : {0}".format(count).encode("utf-8")
            # str → byte

            # print(msg)

            sender_sock.sendto(msg,(host,port))

            count += 1

            time.sleep(1)

    return

if __name__ == "__main__":
    main()