import socket
import random

QUEUE_SIZE = 5

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good",
    "Very doubtful."
]

def server():
    """
    Runs a Magic 8-ball server that listens for client questions and sends back random answers.
    :return:
    """
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('', 5000))
    serv.listen(QUEUE_SIZE)
    print("server is listening on port 5000...")

    while True:
        conn, addr = serv.accept()
        print(f'Connected: {addr}')
        from_client = ''

        while True:
            data = conn.recv(4096)
            if not data:
                break

            from_client += data.decode()
            print(f"Received question: {from_client}")
            answer = random.choice(responses)
            print(f"Answer: {answer}")

            conn.send(f"{answer}".encode())

        conn.close()
        print("Client disconnected")


if __name__ == '__main__':
    server()
