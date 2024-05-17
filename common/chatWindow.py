from typing import Callable, Any
import tkinter as tkt
from socket import socket as Socket
from common.window import Window
from common.defaultParams import * 
from common.defaultParams import TEXT_COLOR, TEXT_COLOR_DARK, BACKGROUND_COLOR, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR

CHAT_WINDOW_DIMS: tuple[int, int] = (640, 350)
CHAT_WINDOW_TITLE: str = "Chat"

class ChatWindow(Window):
    # Constructs the complete chat window for the server
    def __init__(self, closeCallback: Callable[[], Any], socket: Socket, sendCallback: Callable[[Socket, tkt.Entry], None]) -> None:
        # Builds the underlying window
        Window.__init__(self, CHAT_WINDOW_DIMS[0], CHAT_WINDOW_DIMS[1], CHAT_WINDOW_TITLE, closeCallback)
        # Set the window's background
        self.window.configure(bg=BACKGROUND_COLOR)
        # Configuration of the grid for the window 
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        # Base panel to hold all the different widgets
        panelChat: tkt.Frame = tkt.Frame(self.window, bg=BACKGROUND_COLOR)
        panelChat.grid(column=0, row=0, sticky='nsew', padx=4, pady=4)
        # Configuration of the grid for the panel 
        panelChat.grid_columnconfigure(0, weight=1)
        panelChat.grid_rowconfigure(0, weight=1)
        panelChat.grid_rowconfigure(1, weight=1)
        # First panel to hold the chat screen and input
        panelChatText: tkt.Frame = tkt.Frame(panelChat, bg=BACKGROUND_COLOR)
        panelChatText.grid(column=0, row=0, sticky='sew', padx=4, pady=4)
        # Configuration of the grid for the text panel
        panelChatText.grid_columnconfigure(0, weight=1)
        panelChatText.grid_rowconfigure(0, weight=1)
        panelChatText.grid_rowconfigure(1, weight=1)
        # Second panel to hold the two buttons
        panelChatButtons: tkt.Frame = tkt.Frame(panelChat, bg=BACKGROUND_COLOR)
        panelChatButtons.grid(column=0, row=1, sticky='new', padx=4, pady=4)
        # Configuration of the grid for the button panel
        panelChatButtons.grid_rowconfigure(0, weight=1)
        panelChatButtons.grid_columnconfigure(0, weight=1)
        panelChatButtons.grid_columnconfigure(1, weight=1)
        # Listbox to show the chat's messages
        self.messageList: tkt.Listbox = tkt.Listbox(panelChatText, borderwidth=0, highlightthickness=0, fg=TEXT_COLOR, bg=SECONDARY_COLOR ,yscrollcommand=tkt.Scrollbar(panelChatText).set)
        self.messageList.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        self.messageList.grid(column=0, row=0, sticky='new', padx=2, pady=2)
        # Message input as an entry 
        self.messageIn: tkt.Entry = tkt.Entry(panelChatText, borderwidth=0, highlightthickness=0, fg=TEXT_COLOR, bg=SECONDARY_COLOR)
        self.messageIn.insert(0, "Inserisci il messaggio")
        self.messageIn.bind('<FocusIn>', lambda e: self.entryInCallback(e, "Inserisci il messaggio"))
        self.messageIn.bind('<FocusOut>', lambda e: self.entryOutCallback(e, "Inserisci il messaggio"))
        self.messageIn.bind('<Return>', lambda _e: sendCallback(socket, self.messageIn))
        self.messageIn.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        self.messageIn.grid(column=0, row=1, padx=2, pady=2, sticky='sew')
        self.messageIn.focus()
        # Button to quit the chat 
        buttonQuit: tkt.Button = tkt.Button(panelChatButtons, text="Quit", borderwidth=0, highlightthickness=0, command=self.close, fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR)
        buttonQuit.bind("<FocusIn>", lambda _e: buttonQuit.configure(fg=TEXT_COLOR, bg=ACCENT_COLOR))
        buttonQuit.bind("<FocusOut>", lambda _e: buttonQuit.configure(fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR))
        buttonQuit.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        buttonQuit.grid(column=0, row=0, padx=2, pady=2, sticky='nsw')
        # Button to send the message
        buttonSend: tkt.Button = tkt.Button(panelChatButtons, text="Send", borderwidth=0, highlightthickness=0, command=lambda: sendCallback(socket, self.messageIn), fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR)
        buttonSend.bind("<FocusIn>", lambda _e: buttonSend.configure(fg=TEXT_COLOR, bg=ACCENT_COLOR))
        buttonSend.bind("<FocusOut>", lambda _e: buttonSend.configure(fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR))
        buttonSend.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        buttonSend.grid(column=1, row=0, padx=2, pady=2, sticky='nse')
