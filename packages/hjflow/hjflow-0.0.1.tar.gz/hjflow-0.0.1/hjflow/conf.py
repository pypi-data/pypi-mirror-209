
from collections import OrderedDict
import hjson

class Conf(OrderedDict):

    def __init__(self, ctx):

        with open(ctx.args.config_file) as f:
            data = hjson.load(f)

        super().__init__(data)

