# Final Project: Arithmetic Math Game, by Joe Nguyen and Charles Bolt.
# ClientGame.py
# Date: 04/28/22
# Description: This is the client-side game.

import socket
import datetime
import time

# default values
IP = "127.0.0.1"
PORT = 12000
MODE = False
GAMEMODE = 0

# create a socket
print('Welcome to the simple arrithmetic challenge \n - Press x if you want to exit \n')
print()
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ready = input('Are you ready to practice? (Y/N) ')


if ready[0].lower() == 'y':
    MODE = True
    
    # inital question
    message = input('what is 1 + 2? ')

    if message == '3':
        print('Correct! Let\'s get started!')
        GAMEMODE = int(input('Choose a game mode: \n 1. Practice in Timed \n 2. Countdown Challenge \n'))
    else:
        print("Incorrect!")
        MODE = False
        socket.sendto('x'.encode('utf-8'), (IP, PORT))     

elif ready[0].lower() == 'n': 
    MODE = False
    socket.sendto(ready[0].encode('utf-8'), (IP, PORT))
else:
    print('Invalid input')
    MODE = False
    socket.sendto('x'.encode('utf-8'), (IP, PORT))

correct = 0
total = 0

if GAMEMODE == 1: 
    while MODE:
        message = 'The answer is correct. Onto next question.'
        socket.sendto(message.encode('utf-8'), (IP, PORT))
        # get the question from the server
        data, address = socket.recvfrom(2048)
        text = data.decode('utf-8')
        # split the received data into question and answer
        prompt = list(text.partition(' = '))

        # begin timer
        start = time.time()
        userAns = input("What is {}? ".format(prompt[0]))
        
        # loop for incorrect answers
        WRONG_ANSWER = False
        while userAns != prompt[2]:
            print('Incorrect! Try again. Press x if you want to exit. \n')
            userAns = input("What is {}? ".format(prompt[0]))
            if userAns == 'x':
                MODE = False
                userResponse = "User exited the game."
                socket.sendto(userResponse.encode('utf-8'), (IP, PORT))
                WRONG_ANSWER = True
                break
        # end timer
        end = time.time()

        if WRONG_ANSWER:
            break

        print('Correct!')
        print('Time/Question: {:.2f} seconds'.format(end - start))
        total += end - start
        correct += 1
elif GAMEMODE == 2:
    # User enters countdown time
    userTime = int(input('Enter countdown time: '))
    startTime = time.time()

    while MODE and time.time() - startTime < userTime:
        message = 'The answer is correct. Onto next question.'
        socket.sendto(message.encode('utf-8'), (IP, PORT))
        
        data, address = socket.recvfrom(2048)
        text = data.decode('utf-8')
        prompt = list(text.partition(' = '))

        userAns = input("What is {}? ".format(prompt[0]))
        # end the loop when time is up
        
        
        WRONG_ANSWER = False

        while userAns != prompt[2]:
            print('Incorrect! Try again. Press x if you want to exit. \n')
            userAns = input("What is {}? ".format(prompt[0]))
            if userAns == 'x':
                MODE = False
                userResponse = "User exited the game."
                correct -= 1
                socket.sendto(userResponse.encode('utf-8'), (IP, PORT))
                break
        if WRONG_ANSWER:
            break

        print('Correct!')
        correct += 1
    print('Time\'s up! Game over!')
    
else:
    print('Invalid game mode')
    print('Try again by exiting and restarting the program') 
    correct = 0
    MODE = False

if correct == 0:
    # if user exits the game without any questions answered
    print('No questions answered on time')
    if MODE == True:
        print('Game ended')
    else:
        print('Game ended')
else:
    print('You got {} correct!'.format(correct))

    # Converts seconds to minutes and seconds using datetime for timed mode
    if GAMEMODE == 1:
        total = datetime.timedelta(seconds=int(total))
        print('Total answered time: {}'.format(total))
        print('Average correct answer time: {:.2f} seconds\n'.format(total/(correct)))
    # Converts seconds to minutes and seconds using datetime for countdown mode
    elif GAMEMODE == 2:
        print("You answered {} correctly on time\n".format(correct - 1))
        print("Average time per question: {:.2f} seconds\n".format(total/(correct - 1)))
   
print('See you next time!!!')       
print('Connection Closed')
socket.close()

