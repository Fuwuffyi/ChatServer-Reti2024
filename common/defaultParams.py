# Used to declare variables as const
# (doesn't really do anything, it's just type annotation)
from typing import Final
# Used to generate color palettes
import colorsys

# Buffer size for socket communication
BUFFER_SIZE: Final[int] = 1024

# Default settings for client/server stuff
DEFAULT_IP: Final[str] = "127.0.0.1"
DEFAULT_PORT: Final[str] = "53000"
DEFAULT_NAME: Final[str] = "Username"

# Some colors for the UI
STATUS_COLOR: Final[str] = "black"
ERROR_COLOR: Final[str] = "red"

# Command related constants
COMMAND_PREFIX: Final[str] = "/"
COMMAND_QUIT: Final[str] = "quit"
