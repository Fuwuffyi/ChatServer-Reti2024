#!/usr/bin/env python3

from socket import AF_INET, SOCK_STREAM
from socket import socket as Socket
import socket
import errno
import tkinter as tkt
from threading import Thread
from common.chatLoginWindow import ChatLoginWindow
from common.chatWindow import ChatWindow
from common.defaultParams import BUFFER_SIZE, COMMAND_PREFIX, COMMAND_QUIT

# Whenever the chat closes this function gets called
def closeChatCallback(client: Socket) ->None:
    client.send(bytes(COMMAND_PREFIX + COMMAND_QUIT, "utf8"))
    client.close()

def serverConnectCallback(win: ChatLoginWindow, ip: str, port: int, name: str) -> None:
    # Create the connection socket
    clientSocket: Socket = Socket(AF_INET, SOCK_STREAM)
    try:
        # Attempt the connection
        clientSocket.connect((ip, port))
        clientSocket.send(bytes(name, "utf8"))
        # Close the login window
        win.close()
        # Create the chat's window
        chatWindow: ChatWindow = ChatWindow(lambda: closeChatCallback(clientSocket), clientSocket, sendMessageCallback)
        # Start the chat thread
        collectorThread: Thread = Thread(target=lambda: messageCollector(clientSocket, chatWindow.messageList))
        collectorThread.start()
        # Open the chat window
        chatWindow.finishWindow()
        # When the chat ends, close it
        chatWindow.close()
        collectorThread.join()
        # Handle errors in case it could not find the server socket
    except socket.error as error:
        if error.errno == errno.ECONNREFUSED:
            win.setStatusMessage("Connection refused from server!", True)
    except Exception as e:
        print(e)

def sendMessageCallback(clientSocket: Socket, input: tkt.Entry) -> None:
    msg: str = input.get()
    # If the message is not a command, send it to the server
    if not COMMAND_PREFIX in msg:
        clientSocket.send(bytes(input.get(), "utf8"))
        input.delete(0, "end")
    elif msg == COMMAND_PREFIX + COMMAND_QUIT:
        closeChatCallback(clientSocket)

def messageCollector(clientSocket: Socket, chatListbox: tkt.Listbox) -> None:
    chatShouldClose: bool = False
    while not chatShouldClose:
        try:
            # Read the message from the server
            msg: str = clientSocket.recv(BUFFER_SIZE).decode("utf8")
            if not COMMAND_PREFIX in msg:
                chatListbox.insert(tkt.END, msg)
            # Command handling
            elif msg == COMMAND_PREFIX + COMMAND_QUIT:
                chatShouldClose = True
                clientSocket.send(bytes(COMMAND_PREFIX + COMMAND_QUIT, "utf8"))
        except Exception:
            chatShouldClose = True

if __name__ == "__main__":
    chatLoginWindow: ChatLoginWindow = ChatLoginWindow(serverConnectCallback)
    chatLoginWindow.finishWindow()
