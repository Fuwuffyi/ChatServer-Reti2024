from typing import Callable, Any
import tkinter as tkt
from socket import socket as Socket
from common.window import Window
from common.defaultParams import * 

CHAT_WINDOW_DIMS: tuple[int, int] = (640, 350)
CHAT_WINDOW_TITLE: str = "Chat"

class ChatWindow(Window):
    def __init__(self, closeCallback: Callable[[], Any], socket: Socket, sendCallback: Callable[[Socket, tkt.Entry], None]) -> None:
        Window.__init__(self, CHAT_WINDOW_DIMS[0], CHAT_WINDOW_DIMS[1], CHAT_WINDOW_TITLE, closeCallback);
        
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        panelChat: tkt.Frame = tkt.Frame(self.window)
        panelChat.grid(column=0, row=0, sticky='nsew', padx=4, pady=4)
        
        panelChat.grid_columnconfigure(0, weight=1)
        panelChat.grid_rowconfigure(0, weight=1)
        panelChat.grid_rowconfigure(1, weight=1)
        
        panelChatText: tkt.Frame = tkt.Frame(panelChat)
        panelChatText.grid(column=0, row=0, sticky='sew', padx=4, pady=4)

        panelChatText.grid_columnconfigure(0, weight=1)
        panelChatText.grid_rowconfigure(0, weight=1)
        panelChatText.grid_rowconfigure(1, weight=1)
        
        panelChatButtons: tkt.Frame = tkt.Frame(panelChat)
        panelChatButtons.grid(column=0, row=1, sticky='new', padx=4, pady=4)
        panelChatButtons.grid_rowconfigure(0, weight=1)
        panelChatButtons.grid_columnconfigure(0, weight=1)
        panelChatButtons.grid_columnconfigure(1, weight=1)

        self.messageList: tkt.Listbox = tkt.Listbox(panelChatText, height=15, yscrollcommand=tkt.Scrollbar(panelChatText).set)
        self.messageList.grid(column=0, row=0, sticky='new', padx=2, pady=2)
       
        self.messageIn: tkt.Entry = tkt.Entry(panelChatText)
        self.messageIn.insert(0, "Inserisci il messaggio")
        self.messageIn.bind('<FocusIn>', lambda e: self.entryInCallback(self.messageIn, "Inserisci il messaggio"))
        self.messageIn.bind('<FocusOut>', lambda e: self.entryOutCallback(self.messageIn, "Inserisci il messaggio"))
        self.messageIn.grid(column=0, row=1, padx=2, pady=2, sticky='sew')
        self.messageIn.focus()
        
        buttonQuit: tkt.Button = tkt.Button(panelChatButtons, text="Quit", command=self.close)
        buttonQuit.grid(column=0, row=0, padx=2, pady=2, sticky='nsw')

        buttonSend: tkt.Button = tkt.Button(panelChatButtons, text="Send", command=lambda: sendCallback(socket, self.messageIn))
        buttonSend.grid(column=1, row=0, padx=2, pady=2, sticky='nse')
