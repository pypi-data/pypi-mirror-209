from .agpl import getAGPL
from .apache import getApache
from .bsd import getBSD
from .cc0 import getCC0
from .epl import getEPL
from .gnu import getGNU
from .lgpl import getLGPL
from .mit import getMIT
from .wtfpl import getWTFPL

__version__ = "1.0.0"

if __name__ == "__main__":
    print(f"Licensio - {__version__}")