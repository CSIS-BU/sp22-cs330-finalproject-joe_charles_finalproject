# Final Project: Arithmetic Math Game, by Joe Nguyen and Charles Bolt.
# ServerGame.py
# Date: 04/28/22
# Description: This is the server-side of the game.

import socket
import random

# Get answer for addition
def add():
    x = random.randint(2, 100)
    y = random.randint(2, 100)
    prompt = '{} + {} = {}'.format(x, y, x + y)
    return prompt

# Get answer for subtraction
def sub():
    x = random.randint(2, 100)
    y = random.randint(2, 100)
    x, y = sorted([x, y])
    prompt = '{} - {} = {}'.format(y, x, y - x)
    return prompt

# Get answer for multiplication
def mult():
    x = random.randint(2, 12)
    y = random.randint(2, 100)
    prompt = '{} * {} = {}'.format(x, y, x * y)
    return prompt

# Get answer for division, which is multiplication by inverse
def div():
    x = random.randint(2, 12)
    y = random.randint(2, 100)
    z = x * y
    prompt = '{} / {} = {}'.format(z, x, y)
    return prompt

# Function to choose a random question
def choose_test():
    question = random.randint(1, 4)
    if question == 1:
        prompt = add()
    elif question == 2:
        prompt = sub()
    elif question == 3:
        prompt = mult()
    else:
        prompt = div()
    return prompt

# Define the server's IP and port
IP = "127.0.0.1"
PORT = 12000

# Create a socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

# Get ready to receive data
print('Server Listening At {}'.format(socket.getsockname()))

while True:
    # Receive data
    messageBytes, address = socket.recvfrom(2048)
    messageString = messageBytes.decode('utf-8')
    print('Received from client {} : {}'.format(address, messageString))
    
    # Shuts down server when receiving invalid message
    if messageString[0]=='n':
        break
    elif messageString[0]=='x' or messageString[0].lower()=='u':
        break
    
    # Get the question to send to client
    prompt = choose_test()
    # Send the question to client
    socket.sendto(prompt.encode(), address)

# Close the socket
print('Connection Closed')
socket.close()
