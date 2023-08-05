

import argparse

class Args:

    def __init__(self, ctx):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-c', dest='config_file', help='configuration file', type=str, required=True
        )
        self.args = self.parser.parse_args()

    def __getattr__(self, attr):
        if hasattr(self.args, attr):
            return getattr(self.args, attr)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")

