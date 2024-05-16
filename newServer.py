#!/usr/bin/env python3

from socket import AF_INET, AddressInfo, socket, SOCK_STREAM
from threading import Thread
from common.defaultParams import *

def handleClient(client: socket) -> None:
    name: str = connectedClients[client][1]
    clientQuit: bool = False
    # Listen for messages while the client is still up
    while not clientQuit:
        try:
            # Read the message's bytes and convert it to string
            msgBytes: bytes = client.recv(BUFFER_SIZE)
            msg: str = msgBytes.decode("utf8")
            # If it's not a command broadcast the message to everyone
            if not COMMAND_PREFIX in msg:
                print(f"{name}: {msg}")
                broadcast(f"{name}: {msg}")
            # Check quit commad
            elif msg == COMMAND_PREFIX + COMMAND_QUIT:
                # Print the message for everyone
                print(f"User {name}:{connectedClients[client][0]} has left the chat.")
                # Remove it from the local dictionary
                del connectedClients[client]
                # Close the local client socket
                client.close()
                # Broadcast to all remaining clients
                broadcast(f"{name} ha abbandonato la chat.")
                clientQuit = True
        except Exception as e:
            # If any exception happens on the current client, quit the thread
            print(e)
            clientQuit = True

def broadcast(msg: str):
    # Loop over all clients and send the broadcasted encoded message
    for client in connectedClients:
        client.send(bytes(msg, "utf8"))

if __name__ == "__main__":
    # Dictionary to keep all the clients in one structure
    connectedClients: dict[socket, tuple[AddressInfo, str]] = {}
    # Create the local server socket
    server: socket = socket(AF_INET, SOCK_STREAM)
    server.bind(("", int(DEFAULT_PORT)))
    server.listen(5)
    print(f"Local server created at port {DEFAULT_PORT}")
    # List of all the run connections
    clientThreads: list[Thread] = []
    shouldClose: bool = False
    # Start accepting connections
    while not shouldClose:
        try:
            # When a new client joins, get the data
            clientData: tuple[socket, AddressInfo] = server.accept()
            clientSocket: socket = clientData[0]
            clientAddressInfo: AddressInfo = clientData[1]
            # Read the new client's name and broadcast it to the chat
            name: str = clientSocket.recv(BUFFER_SIZE).decode("utf8")
            print(f"User {clientAddressInfo} has joined the chat as {name}.")
            # Load the client in our client dictionary and start listening for his messages
            connectedClients[clientSocket] = (clientAddressInfo, name)
            # Send the entry message to the clients
            broadcast(f"{name} si è unito alla chat")
            # Start the client thread
            clientThread: Thread = Thread(target=lambda: handleClient(clientSocket))
            clientThreads.append(clientThread)
            clientThread.start()
        except KeyboardInterrupt:
            # In case there is a keyboard interrupt, end the communications
            shouldClose = True
        except Exception as e:
            # In any exception, end the communications
            print(e)
            shouldClose = True
    # Send the quit message to all clients to make sure they all shut down
    for client in connectedClients:
        client.send(bytes(COMMAND_PREFIX + COMMAND_QUIT, "utf8"))
    # Join all the threads as the server shuts down
    for clientThread in clientThreads:
        clientThread.join()
    # End of the server
    server.close()
