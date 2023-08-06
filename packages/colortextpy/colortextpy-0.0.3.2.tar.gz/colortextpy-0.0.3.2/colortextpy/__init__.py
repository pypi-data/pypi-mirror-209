__version__ = "0.0.3.2"

from .color import Color
from .ansicolor import Fore, Back, Style, AnsiColor, RESET_ALL
from .colorizer import ColorStream, colorize
from .printer import Printer, colorprint