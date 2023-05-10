import time
import types
import random
class Grade:
    def __init__(self) -> None:
        self.Score=0
        self.Points=0
    def correct(self,worth: int=1):
        self.Score+=worth
        self.Points+=worth
    def incorrect(self,worth: int=1):
        self.Points+=worth
def Printing(String:str,delay:float=0.0625,enddelay:float=1):
    for i in String:
        print(i,end="",flush=True)
        time.sleep(delay)
    time.sleep(enddelay)
PointsDictionary={"Math Question":Grade(),"Rotation Question":Grade(),"Logic Question":Grade()}
Tautologies=[]
Fallacies=[]
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
        Printing("Unfortunately, that answer is not correct.\n",enddelay=2)
        Printing("The correct awnser is {}",eval(Operations[Choice].format(a,b)))
        PointsDictionary["Math Question"].incorrect()
    else:
        Printing("Correct\n")
        PointsDictionary["Math Question"].correct()
def RotationOption():
    global PointsDictionary
    nums=[]
    Size=random.randint(5,10)
    for i in range(Size):
        nums.append(random.randint(1,100))
    Index=random.randint(0,Size-1)
    Direction=random.randint(0,1)
    NumofRots=random.randint(1,Size-1)
    Printing("My list of numbers currently equals {}\n".format(nums))
    Printing("Now I decide to Rotate my list {} times {}\n".format(NumofRots,["left","right"][Direction]),enddelay=2)
    RotResults=[]
    if Direction:
        for i in range(NumofRots):
            nums=nums[-1:] + nums[:-1]
            RotResults.append("Rotation {}: {}, Element {} is {}\n".format(i+1,nums,Index+1,nums[Index]))
    else:
        for i in range(NumofRots):
            nums=nums[1:] + nums[:1]
            RotResults.append("Rotation {}: {}, Element {} is {}\n".format(i+1,nums,Index+1,nums[Index]))
    Printing("I just finished rotating the list.\n",enddelay=2)
    Printing("Now, what is element {} (element 1 is the first element, as we are not using zero indexing) of the new list: ".format(Index+1))
    x=int(input())
    if x==nums[Index]:
        Printing("You are correct",enddelay=2)
        PointsDictionary["Rotation Question"].correct()
    else:
        Printing("That is incorrect\n",enddelay=2)
        Printing("I will show you the rotations\n")
        for i in RotResults:
            Printing(i,enddelay=2)
        PointsDictionary["Rotation Question"].incorrect()
def LogicTest():
    Printing("I am thinking of a random kid's grade. If you are within 10 of his range, you will get a point. If you are greater than him, I will give you two points\n")
    Printing("What is your average grade: ")
    KidsGrade=random.randint(60,100)
    UserGrade=int(input())
    if abs(KidsGrade-UserGrade)<10:
        Printing("Your getting about the same grade as he is.\n")
        PointsDictionary["Logic Question"].correct()
    elif KidsGrade>UserGrade:
        Printing("You can do better next time.\n")
        PointsDictionary["Logic Question"].incorrect()
    else:
        Printing("Wow! Your doing better than he is.\n")
        PointsDictionary["Logic Question"].correct(2)
Printing("Welcome to the J Menu\n",enddelay=2)
while True:
    LogicTest()

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