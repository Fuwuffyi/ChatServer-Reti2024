from typing import Callable, Any
import tkinter as tkt

from common.defaultParams import TEXT_COLOR, TEXT_COLOR_DARK, SECONDARY_COLOR, ACCENT_COLOR

WINDOW_DELETE_PROTOCOL: str = "WM_DELETE_WINDOW"

class Window:
    # Constructor for the window class
    def __init__(self, width: int, height: int, title: str, closeCallback: Callable[[], Any] | None = None) -> None:
        self.title: str = title
        self.closeCallback: Callable[[], Any] | None = closeCallback
        # Create a new window with dimensions
        self.window: tkt.Tk = tkt.Tk()
        self.changeDims(width, height)
        # Add a closing callback
        self.window.protocol(WINDOW_DELETE_PROTOCOL, self.close)

    # Starts the window loop
    def finishWindow(self) -> None:
        self.window.mainloop()

    # Changes the window's dimensions
    def changeDims(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.window.geometry(f"{width}x{height}")

    # Set an entry's default value if they haven't been filled yet
    def entryOutCallback(self, event: tkt.Event, default: str) -> None:
        entry: tkt.Entry = event.widget
        entry.configure(fg=TEXT_COLOR, bg=SECONDARY_COLOR)
        if entry.get() == '':
            entry.insert(0, default)

    # Clear an entry's values if they haven't been filled yet
    def entryInCallback(self, event: tkt.Event, default: str) -> None:
        entry: tkt.Entry = event.widget
        entry.configure(fg=TEXT_COLOR_DARK, bg=ACCENT_COLOR)
        if entry.get() == default:
            entry.delete(0, "end")

    def resizeFontCallback(self, event: tkt.Event):
        # Get the width and height of the container
        container_width: int = self.window.winfo_width() 
        container_height: int = self.window.winfo_height()
        # Calculate a suitable font size based on container dimensions
        new_font_size: int = min(container_width, container_height) // 40
        # Configure the element font with the new font size
        event.widget.configure(font=("Noto Sans Mono", new_font_size))

    def close(self) -> None:
        # If a custom close callback has been defined, use that too
        if self.closeCallback != None:
            self.closeCallback()
        # Destroy the underlying window
        self.window.destroy()
