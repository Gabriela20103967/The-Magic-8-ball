import signal
import time

def signal_handler(sig, frame):
    """
    Handles termination signals (e.g., SIGINT) gracefully.
    :param sig:
    :param frame:
    """
    print(f'Received signal: {sig}. Exiting.')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to exit the process.')

while True:
    time.sleep(1)
