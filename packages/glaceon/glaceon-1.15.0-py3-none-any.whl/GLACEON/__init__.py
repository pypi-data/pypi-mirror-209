__title__ = 'glaceon'
__author__ = 'Zappy'
__version__ = '1.15.0'

CURRENT_VERSION = '1.15.0'

from .cli import *
from .gflask import *

g = cli(debug=True, speed=5)


if __version__ < CURRENT_VERSION:
    g.print("ERROR", 'Version Out-of-Date! Please upgrade by using: \"python.exe -m pip install -U glaceon\"')