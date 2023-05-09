'''
Menu #1 - A menu with 5 options (including a quit option). 
One of the options must be mathematical in nature (basic calculator, tip calculator, grade calculator, etc…)
One of the options must involve lists
One of the options must involve conditional statements (ifs, elses, elifs)
One of the options must involve loops

Menu #2 - A menu with 7 options (including a quit option).
All five options from Menu #1, plus
An option that involves some sort of guessing game
Something that gets personal information from the user like name, age, favorite color, etc… and uses it throughout all programs

Menu #3 - A menu with 9 options (including a quit option).
All seven options from Menu #2, plus
An option that involves a one-player game like rock, paper, scissors
An option that includes a simple chatbot
'''

import time
import types
import random
class Grade:
    def __init__(self) -> None:
        self.Score=0
        self.Points=0
    def correct(self):
        self.Score+=1
        self.Points+=1
    def incorrect(self):
        self.Points+=1
def Printing(String:str,delay:float=0.0625,enddelay:float=1):
    for i in String:
        print(i,end="",flush=True)
        time.sleep(delay)
    time.sleep(enddelay)
PointsDictionary:dict={"Math Question":Grade(),"List Question":Grade()}
def MathQuestion():
    global PointsDictionary
    Choice=0
    Operations=["{}+{}","{}-{}","{}*{}","{}//{}","{}%{}","{}/{}"]
    a=random.randint(1,10)
    b=random.randint(1,10)
    if (Choice==3):
        print("The quotient of {} divided by {}=")
    else:
        Printing(Operations[Choice].format(a,b)+"=")
    c=float(input())
    if c!=eval(Operations[Choice].format(a,b)):
        Printing("Unfortunately, that answer is not correct.\n")
        PointsDictionary["Math Question"].incorrect()
    else:
        Printing("Correct\n")
        PointsDictionary["Math Question"].correct()
def MathDataSetQuestion():
    x=None
Printing("Welcome to the Tool\n",enddelay=2)
'''
while True:
    MathQuestion()
'''