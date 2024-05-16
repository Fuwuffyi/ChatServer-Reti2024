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
COLOR_PALETTE: Final[list[str]] = generatePalette()
TEXT_COLOR: Final[str] = COLOR_PALETTE[0]
BACKGROUND_COLOR: Final[str] = COLOR_PALETTE[1]
PRIMARY_COLOR: Final[str] = COLOR_PALETTE[2]
SECONDARY_COLOR: Final[str] = COLOR_PALETTE[3]
ACCENT_COLOR: Final[str] = COLOR_PALETTE[4]
# Some colors for the status messages 
STATUS_COLOR: Final[str] = TEXT_COLOR
ERROR_COLOR: Final[str] = "red"

# Command related constants
COMMAND_PREFIX: Final[str] = "/"
COMMAND_QUIT: Final[str] = "quit"
