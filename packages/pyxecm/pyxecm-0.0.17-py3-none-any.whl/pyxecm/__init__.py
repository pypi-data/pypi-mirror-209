import logging
import os

# pyxecm packages
from pyxecm.main import *
from pyxecm.k8s import *
from pyxecm.otac import *
from pyxecm.otcs import *
from pyxecm.otds import *
from pyxecm.otiv import *
from pyxecm.otpd import *
from pyxecm.payload import *
from pyxecm.translate import *
from pyxecm.web import *

logging.basicConfig(
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    datefmt="%d-%b-%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(os.path.basename(__file__))