# Final Project: Arithmetic Math Game, by Joe Nguyen and Charles Bolt.
# GameEngine.py
# Date: 04/16/22
# Description: This is the main game engine for the Arithmetic Math Game.

from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox


class SelectionPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Arithmetic Practice")
        mainframe = tk.Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)
        tkvar = StringVar(self)
        choices = {'add_sub', 'add'}
        Label(mainframe, text="Choose a test").grid(row=1, column=1)
        popupMenu = OptionMenu(mainframe, tkvar, *choices)
        popupMenu.config(width=20)

        popupMenu.grid(row=2, column=1)


        def start_practice():
            print(tkvar.get())
            time = 180

            tol = 0.1 # approximation error tol
            root = Tk()
            choices_dict = {'add_sub': ['add', 'sub', 'mult'],
                            'add': ['add']}

            app = App(root, time, tol, choices_dict[tkvar.get()])
            root.mainloop()

        MyButton1 = Button(mainframe, text="Submit", width=10, command=start_practice)
        MyButton1.grid(row=3, column=1)



class App(tk.Frame):
    def __init__(self, parent, time, tol, choices):
        tk.Frame.__init__(self, parent)
        self.count = time
        self.scr = 0
        self.ans = 3
        self.exact = True
        self.tol = tol

        self.choices = choices

        self.parent = parent

        self.parent.title("Arithmetic Practice")
        self.parent.geometry("700x260")

        self.prompt = Label(self, text="1+2=", bg="gainsboro", width=10, font = ("Roman", 40), anchor = 'e') 

        self.answer = Entry(self, font=("Roman", 40), width=20)
        self.answer.bind("<Return>", self.check_answer)


        self.timer = Label(self, text="Seconds left: 1")
        self.score = Label(self, text="score: 0")

        # motive = "[Chorus] Just like Citadel, Jane Street, Two Sigma, Akuna" \
        #          "\nAll I need, yeah, you're all I need."

        # self.motive = Label(self, text=motive, font=("Helvetica", 10, "italic"))

        self.correct_ans = Label(self, font=("Roman", 20))

        self.prompt.grid(row=0)
        self.answer.grid(row=0, column=1)
        self.score.grid(row=1)
        self.timer.grid(row=1, column=1)
        self.correct_ans.grid(row=2)
        self.motive.grid(row=2, column=1)
        self.pack()

        self.onUpdate()
    # Game Engine.
    def next_question(self):
        def add():
            x = random.randint(2, 100)
            y = random.randint(2, 100)
            prompt = '{} + {} ='.format(x, y)
            self.ans = x + y
            return prompt

        def sub():
            x = random.randint(2, 100)
            y = random.randint(2, 100)
            x, y = sorted([x, y])
            prompt = '{} - {} ='.format(y, x)
            self.ans = y - x
            return prompt
        # get answer for multiplication
        def mult():
            x = random.randint(2, 12)
            y = random.randint(2, 100)
            prompt = '{} x {} ='.format(x, y)
            self.ans = x * y
            return prompt
        # get answer for division, which is multiplication by inverse
        def div():
            x = random.randint(2, 12)
            y = random.randint(2, 100)
            z = x * y
            prompt = '{} / {} ='.format(z, x)
            self.ans = z / x
            return prompt
        this_fn = locals()
        self.tests = [this_fn[i] for i in self.choices]
        
        return random.choice(self.tests)()

    def check_answer(self, event):

        user_ans = float(self.answer.get().strip())
        diff = abs(user_ans - self.ans)
        print('diff:', diff, '|exact?', self.exact, '| tol:', self.tol, '| my ans:', user_ans)

        if diff == 0 or (not self.exact and diff < self.tol):
            self.exact = True
            self.correct_ans["text"] = self.prompt["text"] + ('%.3f'% self.ans)
            prompt = self.next_question()
            self.prompt["text"] = prompt
            self.scr += 1
            self.answer.delete(0, 'end')
        else:
            self.scr -= 0 # No penalty for wrong answer

        self.score["text"] = "score: " + str(self.scr)

    def onUpdate(self):
        # update displayed time
        self.count -=1
        if self.count <= 0:
            messagebox.showinfo("TIME'S UP!", "YOUR SCORE = {}".format(self.scr))
            self.parent.destroy()
        else:
            self.timer['text'] = "Seconds left: " + str(self.count)
            # schedule timer to call myself after 1 second
            self.parent.after(1000, self.onUpdate)

if __name__ == '__main__':
    app = SelectionPage()
    app.mainloop()

