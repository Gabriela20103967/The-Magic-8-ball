import signal
import time

def signal_handler(sig, frame):
    print(f'Received signal: {sig}. Exiting.')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to exit the process.')

while True:
    time.sleep(1)
