
import importlib
import multiprocessing
import sys
import threading

class Flow:

    def __init__(self, ctx):

        self.ctx = ctx
        self.args = ctx.args
        self.conf = ctx.conf
        self.key = ctx.key
        self.opt = ctx.options
        self.pid = ctx.pid

        self.load_modules()


    def load_modules(self):

        modules = {}

        for entry in self.conf['flow']:

            if 'mod' in self.conf['flow'][entry]:

                module = self.conf['flow'][entry]['mod']

                if module not in sys.modules.items():
                    modules[module] = importlib.import_module(module)

        self.modules = modules


    def exec(self):

        for name, data in self.conf['flow'].items():

            data['name'] = name
            data['ctx'] = self.ctx
            data['module'] = self.modules[data['mod']]

            try: data['settings'] = self.conf['settings'][name]
            except: pass

            if 'class' in data:
                func = self.class_runner
            else:
                func = getattr(data['module'], data['func'])

            exec_type = data.get('type', 'call')

            if exec_type == 'spawn':
                self.spawn_process(name, func, data)
            elif exec_type == 'thread':
                self.spawn_thread(name, func, data)
            elif exec_type == 'call':
                func(data)
            else:
                self.fail(f'unknown exec_type: {exec_type}')

    def class_runner(self, data):

        Class = getattr(data['module'], data['class'])
        method = getattr(Class, data['func'])
        obj = Class(data['name'], data)
        method(obj)

    def spawn_process(self, name, func, data):

        process = multiprocessing.Process(name=name, target=func, args=([data]))

        process.start()

    def spawn_thread(self, name, func, data):

        thread = threading.Thread(name='thread', target=func, args=([data]))

        thread.start()
        threading.Thread

