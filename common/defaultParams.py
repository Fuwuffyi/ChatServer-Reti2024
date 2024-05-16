# Used to declare variables as const
# (doesn't really do anything, it's just type annotation)
from typing import Final
from common.colorGen import generatePalette 

# Buffer size for socket communication
BUFFER_SIZE: Final[int] = 1024

# Default settings for client/server stuff
DEFAULT_IP: Final[str] = "127.0.0.1"
DEFAULT_PORT: Final[str] = "53000"
DEFAULT_NAME: Final[str] = "Username"

# Palette stuff
COLOR_PALETTE: Final[dict[str, str]] = generatePalette()
TEXT_COLOR: Final[str] = COLOR_PALETTE['text']
BACKGROUND_COLOR: Final[str] = COLOR_PALETTE['background']
PRIMARY_COLOR: Final[str] = COLOR_PALETTE['primary']
SECONDARY_COLOR: Final[str] = COLOR_PALETTE['secondary']
ACCENT_COLOR: Final[str] = COLOR_PALETTE['accent']

# Some colors for the status messages 
STATUS_COLOR: Final[str] = TEXT_COLOR
ERROR_COLOR: Final[str] = "red"

# Command related constants
COMMAND_PREFIX: Final[str] = "/"
COMMAND_QUIT: Final[str] = "quit"
