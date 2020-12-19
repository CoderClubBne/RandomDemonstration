# Thread demonstration in python.
# Author: Nicholas Curran 2020-12-19

import queue
import threading

def thread_func(q):
    print("Second thread started")
    nextItem = q.get()
    while nextItem != "quit":
        print("Got next item: " + nextItem)
        nextItem = q.get()
    print("Exiting second thread")

theQ = queue.Queue()
t = threading.Thread(target=thread_func, args=(theQ,))
t.start()

# Main loop
print("Main thread start")
inputValue = ""
while inputValue != "quit":
    inputValue = input("Type an item: ")
    theQ.put(inputValue)
print("Main thread finished")

t.join()
print("Program finished")
