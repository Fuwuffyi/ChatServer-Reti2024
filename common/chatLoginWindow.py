from typing import Callable
import re
import tkinter as tkt
from common.window import Window
from common.defaultParams import * 

LOGIN_WINDOW_DIMS: tuple[int, int] = (300, 375)
LOGIN_WINDOW_TITLE: str = "Chat Login"

class ChatLoginWindow(Window):
    def __init__(self, loginOutCallback: Callable[[Window, str, int, str], None]) -> None:
        Window.__init__(self, LOGIN_WINDOW_DIMS[0], LOGIN_WINDOW_DIMS[1], LOGIN_WINDOW_TITLE);

        panelLogin: tkt.Frame = tkt.Frame(self.window)
        panelLogin.pack(fill='both', padx=4, pady=4, expand=True)
       
        self.statusLabelText: tkt.StringVar = tkt.StringVar()
        self.statusLabelText.set("Effettua il login al server.")
        self.statusLabel: tkt.Label = tkt.Label(panelLogin, textvariable=self.statusLabelText)
        self.statusLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
    
        ipLabel: tkt.Label = tkt.Label(panelLogin, text="Server IP: ")
        ipLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
     
        self.ipIn: tkt.Entry = tkt.Entry(panelLogin)
        self.ipIn.insert(0, DEFAULT_IP)
        self.ipIn.bind('<FocusIn>', lambda e: self.entryInCallback(self.ipIn, DEFAULT_IP))
        self.ipIn.bind('<FocusOut>', lambda e: self.entryOutCallback(self.ipIn, DEFAULT_IP))
        self.ipIn.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        self.ipIn.focus()
     
        portLabel: tkt.Label = tkt.Label(panelLogin, text="Server Port: ")
        portLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
    
        self.portIn: tkt.Entry = tkt.Entry(panelLogin)
        self.portIn.insert(0, DEFAULT_PORT)
        self.portIn.bind('<FocusIn>', lambda e: self.entryInCallback(self.portIn, DEFAULT_PORT))
        self.portIn.bind('<FocusOut>', lambda e: self.entryOutCallback(self.portIn, DEFAULT_PORT))
        self.portIn.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
     
        nameLabel: tkt.Label = tkt.Label(panelLogin, text="Username: ")
        nameLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
    
        self.nameIn: tkt.Entry = tkt.Entry(panelLogin)
        self.nameIn.insert(0, DEFAULT_NAME)
        self.nameIn.bind('<FocusIn>', lambda e: self.entryInCallback(self.nameIn, DEFAULT_NAME))
        self.nameIn.bind('<FocusOut>', lambda e: self.entryOutCallback(self.nameIn, DEFAULT_NAME))
        self.nameIn.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
   
        buttonConfirm: tkt.Button = tkt.Button(panelLogin, text="Login", relief="raised", command=self.loginCallback)
        buttonConfirm.pack(side='top', fill='both', expand=True, anchor='nw', padx=2, pady=2);
     
        buttonConfirm: tkt.Button = tkt.Button(panelLogin, text="Cancel", relief='raised', command=self.close)
        buttonConfirm.pack(side='top', fill='both', expand=True, anchor='nw', padx=2, pady=2);

        self.loginOutCallback: Callable[[ChatLoginWindow, str, int, str], None] = loginOutCallback

    def setStatusMessage(self, message: str, error: bool = False):
        self.statusLabel.config(fg=ERROR_COLOR if error else STATUS_COLOR)
        self.statusLabelText.set(message)
    
    def loginCallback(self) -> None:
        # Get the input values
        ipIn: str = self.ipIn.get()
        portIn: str = self.portIn.get()
        nameIn: str = self.nameIn.get()
        # Check if all of the inputs have been set
        if len(ipIn) <= 1 or len(portIn) <= 1 or len(nameIn) <= 1:
            self.setStatusMessage("Non hai inserito uno dei dati!", True)
            return
        # Check if the ip is a valid ip
        if not re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ipIn):
            self.setStatusMessage("L'ip inserito non è valido!", True)
            return
        # Check if the port is a valid port
        if not portIn.isdigit and int(portIn) < 1 and int(portIn) > 65565:
            self.setStatusMessage("La porta inserita non è valida!", True)
            return
        # Check if the username is valid
        if not re.match(r"[A-Za-z0-9_]{4,29}$", nameIn):
            self.setStatusMessage("L'username inserito non è valido!", True)
            return
        # Effettua connessione al server
        self.loginOutCallback(self, ipIn, int(portIn), nameIn)

