# Socket Based Client-Server Chat Application 
## Overview
This project is a simple client-server chat application developed in Python. It utilizes sockets for network communication and Tkinter for a responsive and visually appealing GUI.
## Features
- **Client-Server Architecture**: The application follows a client-server model where multiple clients can connect to a central server to send and receive messages.
- **Socket Communication**: Utilizes Python's `socket` library for handling the network communication between the server and clients.
- **Responsive GUI**: The GUI is created using Tkinter, ensuring a user-friendly and responsive interface.
- **Randomized Colors**: The GUI generates a random color palette every time the client is run.
## Files
The project consists of two main files:
1. **chatServer.py**: This script runs the server that handles incoming client connections and broadcasts messages to all connected clients.
2. **chatClient.py**: This script runs the client that connects to the server, sends messages, and displays received messages in the GUI.
## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- colorsys (usually included with Python)
## Usage
### Server
1. Open a terminal.
2. Navigate to the directory containing `chatServer.py`.
3. Run the server script:
   ```bash
   ./chatServer.py
   # OR
   python chatServer.py
   ```
4. The server will start in a CLI and listen for incoming client connections on the specified port.
### Client
1. Open a terminal.
2. Navigate to the directory containing `chatClient.py`.
3. Run the client script:
   ```bash
   ./chatClient.py
   # OR
   python chatClient.py
   ```
4. A GUI window will open, prompting you to enter the server's IP address and port number.
5. Once connected, a new window will pop up, you can start sending and receiving messages.
### Example Workflow
1. Start the server:
   ```bash
   python chatServer.py
   ```
   The server will output a message indicating it is listening for connections.
2. Start a client:
   ```bash
   python chatClient.py
   ```
   The client GUI will appear. Enter the server's IP address, port number and username to connect.
3. Open additional terminals and start more clients as needed, following the same steps.
4. Send messages from any client, and all connected clients, including the sender, will receive and display the messages.
#### Client Input Notes
- If the client does not provide a valid ip address, port or username (the username must not contain a space, and be between 4 and 30 characters in length), the login page will print out errors in the GUI.
- If the client tries to log in while the server is not active, it will also print out an error to the GUI
## Notes
- This project is for educational purposes and may need enhancements for production use, such as error handling, security improvements, and more robust GUI features.
