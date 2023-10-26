import threading

from cam1 import cam1
from cam2 import cam2
from cam3 import cam3
from cam4 import cam4
from dataServer import data_ser
import socket
# Define a dictionary to hold thread targets and their arguments
ip='192.168.37.238'
threads_data = {
    "Thread 1": (cam1, (11,ip,)),
    "Thread 2": (cam2, (22,ip,)),
    "Thread 3": (cam3, (33,ip,)),
    "Thread 4": (cam4, (44,ip,)),
    "Thread 5": (data_ser, (55,ip,))
}

def run_threads(threads_data):
    threads = {}

    # Create and start the threads
    for thread_name, (target, args) in threads_data.items():
        thread = threading.Thread(target=target, args=args)
        threads[thread] = threads.get(thread,0)
    
        thread.start()
        #threads.append(thread)

    # Wait for all threads to finish
    for thread in threads.keys():
        thread.join()


if __name__ == "__main__":
    run_threads(threads_data)
    print("Both threads have finished.")

