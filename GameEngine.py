# Final Project: Arithmetic Math Game, by Joe Nguyen and Charles Bolt.
# GameEngine.py
# Date: 04/16/22
# Description: This is the main game engine for the Arithmetic Math Game.

import random

from datetime import datetime
import os

# Date-time objective.
def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


class SelectionPage():
    def __init__(self, *args, **kwargs):
        #TODO: Get objective.

    def speak(self, prompt):
        # TODO: Get objective.

    def next_question(self):
        # TODO: Get objective.

        def square():
            # TODO: Calculate squre of a random number.

        def square_root():
            # TODO: Calculate square root of a random number.

        def add():
            # TODO: Calculate sum of two random numbers.

        def sub():
            # TODO: Calculate difference of two random numbers.


        return random.choice(self.tests)()

    def check_answer(self, event):

        #TODO: Check the answers.

if __name__ == '__main__':

    app = SelectionPage()
    app.speak("Welcome to the mental math test. GLHF!")

