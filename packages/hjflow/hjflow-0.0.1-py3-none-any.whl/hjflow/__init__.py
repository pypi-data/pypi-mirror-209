
import os
import secrets

from .args import Args
from .conf import Conf
from .flow import Flow

class HJFlow:

    def __init__(self, options):

        self.pid = os.getpid()
        self.key = secrets.token_bytes(32)
        self.options = options
        self.args = Args(self)
        self.conf = Conf(self)
        self.flow = Flow(self)
        self.run = self.flow.exec

