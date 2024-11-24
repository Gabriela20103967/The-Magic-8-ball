import socket


def player():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5000))
    question = input("Ask the magic 8-ball to know the answer: ")
    sock.send(question.encode())
    from_server = sock.recv(4096)
    sock.close()

    print("The Magic 8-ball answer is: ", from_server.decode())


if __name__ == '__main__':
    player()