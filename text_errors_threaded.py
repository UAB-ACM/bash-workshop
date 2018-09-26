from threading import Thread
from os import getenv
from queue import deque
from time import sleep
from sys import stderr

from twilio.rest import Client


account_sid = getenv('TWILIO_SID')
auth_token = getenv('TWILIO_AUTH_TOKEN')
from_number = getenv('TWILIO_FROM_NUMBER')
to_number =  getenv('TWILIO_TO_NUMBER')
client = Client(account_sid, auth_token)

class InputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.queue = deque()

    def run(self):
        print("thread starting")
        try:
            self.process_input()
        except EOFError:
            return
    
    def process_input(self):
        while True:
            next_line = input()
            self.queue.append(next_line)

def update(queue):
    size = len(thread.queue)
    errors = chunk(thread.queue, size)
    handle_errors(errors)

def handle_errors(errors):
    if len(errors) == 0:
        return
    print(errors, file=stderr)
    client.messages.create(body='\n'.join(errors), to=to_number, from_=from_number)

def chunk(queue, count):
    chunk = []
    for _ in range(count):
        chunk.append( thread.queue.popleft() )
    return chunk


thread = InputThread()
thread.start()

try:
    while thread.is_alive():
        sleep(5)
        update(thread.queue)
except KeyboardInterrupt:
    pass

update(thread.queue)