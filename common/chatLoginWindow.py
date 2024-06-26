from typing import Final, Callable
import re
import tkinter as tkt
from common.window import Window
from common.defaultParams import DEFAULT_IP, DEFAULT_PORT, DEFAULT_NAME, TEXT_COLOR_DARK
from common.defaultParams import TEXT_COLOR, BACKGROUND_COLOR, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, ERROR_COLOR

LOGIN_WINDOW_DIMS: Final[tuple[int, int]] = (300, 375)
LOGIN_WINDOW_TITLE: Final[str] = "Chat Login"

class ChatLoginWindow(Window):
    # Constructor for the login page of our application
    def __init__(self, loginOutCallback: Callable[['ChatLoginWindow', str, int, str], None]) -> None:
        # Creates the underlying window
        Window.__init__(self, LOGIN_WINDOW_DIMS[0], LOGIN_WINDOW_DIMS[1], LOGIN_WINDOW_TITLE);
        # Give the window the default bg color
        self.window.configure(bg=BACKGROUND_COLOR)
        # Basic panel to contain all of our ui elements
        panelLogin: tkt.Frame = tkt.Frame(self.window, bg=BACKGROUND_COLOR)
        panelLogin.pack(fill='both', padx=4, pady=4, expand=True)
        # Status label to tell the user some input errors and such
        self.statusLabelText: tkt.StringVar = tkt.StringVar()
        self.statusLabelText.set("Effettua il login al server.")
        self.statusLabel: tkt.Label = tkt.Label(panelLogin, textvariable=self.statusLabelText, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.statusLabel.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        self.statusLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        # Label for the IP input of the form
        ipLabel: tkt.Label = tkt.Label(panelLogin, text="Server IP: ", bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        ipLabel.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        ipLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        # Input entry for the IP
        self.ipIn: tkt.Entry = tkt.Entry(panelLogin, borderwidth=0, highlightthickness=0, relief='flat', fg=TEXT_COLOR, bg=SECONDARY_COLOR)
        self.ipIn.insert(0, DEFAULT_IP)
        self.ipIn.bind('<FocusIn>', lambda e: self.entryInCallback(e, DEFAULT_IP))
        self.ipIn.bind('<FocusOut>', lambda e: self.entryOutCallback(e, DEFAULT_IP))
        self.ipIn.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        self.ipIn.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        self.ipIn.focus()
        # Label for the port input of the form
        portLabel: tkt.Label = tkt.Label(panelLogin, text="Server Port: ", bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        portLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        portLabel.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        # Input entry for the PORT
        self.portIn: tkt.Entry = tkt.Entry(panelLogin, borderwidth=0, highlightthickness=0, relief='flat', fg=TEXT_COLOR, bg=SECONDARY_COLOR)
        self.portIn.insert(0, DEFAULT_PORT)
        self.portIn.bind('<FocusIn>', lambda e: self.entryInCallback(e, DEFAULT_PORT))
        self.portIn.bind('<FocusOut>', lambda e: self.entryOutCallback(e, DEFAULT_PORT))
        self.portIn.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        self.portIn.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        # Label for the username input of the form
        nameLabel: tkt.Label = tkt.Label(panelLogin, text="Username: ", bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        nameLabel.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        nameLabel.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        # Input entry for the username 
        self.nameIn: tkt.Entry = tkt.Entry(panelLogin, borderwidth=0, highlightthickness=0, relief='flat', fg=TEXT_COLOR, bg=SECONDARY_COLOR)
        self.nameIn.insert(0, DEFAULT_NAME)
        self.nameIn.bind('<FocusIn>', lambda e: self.entryInCallback(e, DEFAULT_NAME))
        self.nameIn.bind('<FocusOut>', lambda e: self.entryOutCallback(e, DEFAULT_NAME))
        self.nameIn.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        self.nameIn.pack(side='top', fill='y', expand=True, anchor='nw', padx=2, pady=2)
        # Button to confirm the login info to the server 
        buttonConfirm: tkt.Button = tkt.Button(panelLogin, text="Login", borderwidth=0, highlightthickness=0, relief="flat", command=self.loginCallback, fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR)
        buttonConfirm.bind("<FocusIn>", lambda e: e.widget.configure(fg=TEXT_COLOR_DARK, bg=ACCENT_COLOR))
        buttonConfirm.bind("<FocusOut>", lambda e: e.widget.configure(fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR))
        buttonConfirm.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        buttonConfirm.pack(side='top', fill='both', expand=True, anchor='nw', padx=2, pady=2);
        # Button to cancel the login and close the window
        buttonCancel: tkt.Button = tkt.Button(panelLogin, text="Cancel", borderwidth=0, highlightthickness=0, relief='flat', command=self.close, fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR)
        buttonCancel.bind("<FocusIn>", lambda e: e.widget.configure(fg=TEXT_COLOR_DARK, bg=ACCENT_COLOR))
        buttonCancel.bind("<FocusOut>", lambda e: e.widget.configure(fg=TEXT_COLOR_DARK, bg=PRIMARY_COLOR))
        buttonCancel.bind('<Configure>', lambda e: self.resizeFontCallback(e))
        buttonCancel.pack(side='top', fill='both', expand=True, anchor='nw', padx=2, pady=2);
        # Sets the login callback for the login button 
        self.loginOutCallback: Callable[[ChatLoginWindow, str, int, str], None] = loginOutCallback
    
    # Changes the login status message in a clear way
    def setStatusMessage(self, message: str, error: bool = False):
        self.statusLabel.config(fg=ERROR_COLOR if error else TEXT_COLOR)
        self.statusLabelText.set(message)
    
    # Method to get all the info when logging in, and checking for their validity
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
        # Connect to the server
        self.loginOutCallback(self, ipIn, int(portIn), nameIn)

