
# HJFlow for Python

## Overview

HJFlow is a framework designed to simplify the creation of Python scripts and programs. The
program flow including executed methods/functions are defined in a file, making it easy to
modify the program's structure and quickly understand the program flow. With HJFlow, complex
projects become more manageable and user-friendly, with a focus on clarity and flexibility.

## Features

HJFlow provides a number of simple but effective mechanisms to facilitate fast
development by enabling easy modification of your entire programs structure.

- Basic framework to get started quickly with any type of program
- Provides basis for configurable program flow and settings handling
- Can facilitate clear division between internal parts of your program
- Support for both single-shot and continuously running programs
- Enables parallel, linear and mixed program execution flows with
  execution types 'spawn', 'thread' and 'call'
- The progam flow is defined in a wonderfully readable HJSON file

## Examples

This is a simple hjflow demo program which consists of four files.

hjflow_demo -- The main script using standard way to initiate a HJFlow program.
```
#!/usr/bin/env python3

from hjflow import HJFlow

hjflow_options = {
    "program_name": "hjflow_demo",
    "program_description": "Simple demo program for HJFlow",
    "program_version": "0.1",
}

hjflow = HJFlow(hjflow_options)

hjflow.run()
```

hjflow_demo.conf -- the configuration and flow file
```
name: "hjflow_demo"               # <- definitions at any level of the configration
                              #    file are reachable from your program code
flow: {                       # <- ordered 'flow' section defines the execution
    first_task: {             # <- name of the step, available in your code
        mod: "task1"          # <- python module file from where to load the code
        class: "Server",      # <- if class is defined, it will be instatiated
        func: "run_server",   # <- this is the method which will be exected
        type: "thread"        # <- use 'spwan' to run in separate process,
    }                         #    'thread' to run in thread and 'call' to
    second_task: {            #    just call the function
        mod: "task2",
        func: "client_function",  # 'second_task' doesn't instantiate an object but
        type: "call",             # instead the main process will just call this
    }                             # function. One useful way to use hjflow is to
}                                 # define your program just as list of calls

settings: {

    socket: "/tmp/hjflow_demo.sock"   # <- this will be reachable from the tasks though
                                  #    the ctx pointer
    first_task: {
        message: "hello",         # <- this block will be automatically visible
    }                             #    to the 'first_task' in data['settings'].
                                  #    the data dict is always passed to the
    second_task: {                #    executed function or method as a parameter
        wait: 3
    }
}
```

task1.py -- implementation of "first_task"
```
import time
from multiprocessing.connection import Listener

class Server:

    def __init__(self, name, data):

        # Name of this module as defined in flow: { name: ... }
        self.name = name

        # Get own settings defined in settings: { name: { ... } }
        self.message = data['settings']['message']

        # We can also access items from the global ctx
        self.sock_path = data['ctx'].conf['settings']['socket']

    def run_server(self):

        self.listener = Listener(self.sock_path, 'AF_UNIX')
        print(f"Server: started listener at {self.sock_path}")

        while True:
            conn = self.listener.accept()
            print(f"Server: connection accepted")

            msg_id = 1

            while True:
                message = (f'msg id: {msg_id}, from: {self.name}, msg: {self.message}')
                print(f'Server: sending messge "{message}"')
                conn.send(message)

                msg_id += 1

                time.sleep(2)

            time.sleep(2)
```

task2.py - implementation of "second_task"
```
import time
from multiprocessing.connection import Client

def client_function(data):

    wait = data['settings']['wait']
    sock = data['ctx'].conf['settings']['socket']

    print(f'Client: waiting for {wait} seconds for server to become ready')

    time.sleep(wait)

    with Client(sock, 'AF_UNIX') as conn:

        print(f'Client: connected')

        while True:
            msg = conn.recv()
            print(f'Client: received message "{msg}"')
```

Running the demo
```
$ ./hjflow_demo -c hjflow_demo.conf
Client: waiting for 3 seconds for server to become ready
Server: started listener at /tmp/hjflow_demo.sock
Client: connected
Server: connection accepted
Server: sending messge "message id: 1, from: first_task, payload: hello"
Client: received message "message id: 1, from: first_task, payload: hello"
Server: sending messge "message id: 2, from: first_task, payload: hello"
Client: received message "message id: 2, from: first_task, payload: hello"
```

