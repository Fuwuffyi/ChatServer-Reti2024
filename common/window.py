from typing import Callable, Any
import tkinter as tkt

WINDOW_DELETE_PROTOCOL: str = "WM_DELETE_WINDOW"

class Window:
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
    def entryOutCallback(self, entry: tkt.Entry, default: str) -> None:
        if entry.get() == '':
            entry.insert(0, default)

    # Clear an entry's values if they haven't been filled yet
    def entryInCallback(self, entry: tkt.Entry, default: str) -> None:
        if entry.get() == default:
            entry.delete(0, "end")

    def close(self) -> None:
        # If a custom close callback has been defined, use that too
        if self.closeCallback != None:
            self.closeCallback()
        # Destroy the underlying window
        self.window.destroy()
