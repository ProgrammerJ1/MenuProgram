import time
import types
import random
import inquirer
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
PointsDictionary={"Math Question":Grade(),"Rotation Question":Grade(),"Logic Question":Grade(),"Guessing Game":Grade()}
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
def BooleanExpressionGenerator()->str:
    numofnums=random.randint(2,5)
    Numbers=[]
    for i in range(numofnums):
        Numbers.append(random.randint(1,100))
    Operators=[]
    for i in range(numofnums-1):
        Operators.append(["+","-","*","/","%"][random.randint(0,4)])
    BooleanExpression="("
    for i in range(numofnums-1):
        BooleanExpression+=str(Numbers[i])
        BooleanExpression+=str(Operators[i])
    BooleanExpression+=str(Numbers[numofnums-1])
    BooleanExpression+=["==",">","<","<=",">="][random.randint(0,4)]
    BooleanExpression+=str(random.randint(0,100**numofnums))
    BooleanExpression+=")"
    return BooleanExpression

def LogicTest():
    TestExpression=""
    if (random.randint(0,1)):
        BitwiseSymbol=["&","|","^"][random.randint(0,2)]
        TestExpression=BooleanExpressionGenerator()+BitwiseSymbol+BooleanExpressionGenerator()
    else:
        TestExpression=BooleanExpressionGenerator()
        TestExpression=TestExpression[1:len(TestExpression)-2]
    Correctness=eval(TestExpression) and inquirer.prompt([inquirer.Confirm("answer",message="Do you believe the expression {} is true".format(TestExpression.replace("&"," and ").replace("|"," or ").replace("^"," xor ")))])["answer"]
    if Correctness:
        Printing("You are correct.",enddelay=2)
        PointsDictionary["Logic Question"].correct()
    else:
        Printing("You are unfortunately incorrect",enddelay=2)
        PointsDictionary["Logic Question"].incorrect()
def GuessingGame():
    Num=random.randint(1,100)
    Printing("I have a number in my head, what is it?: ".format(Num))
    GuessedNum=int(input())
    if GuessedNum==Num:
        Printing("Correct, you get a point\n")
        PointsDictionary["Guessing Game"].correct()
    else:
        Printing("Incorrect, the number was {}\n".format(Num))
        PointsDictionary["Guessing Game"].incorrect()
def Quit():
    #Print all the points and stats of the user
    Printing("Goodbye\n")
    exit(0)
def Menu():
    OptionsDict={
        "Answer a math question for a point":MathQuestion,
        "Answer a rotation question for a point":RotationOption,
        "Answer a logic question":LogicTest,
        "Guess a number for a point":GuessingGame,
        "Quit":Quit
    }
    Printing("Welcome to the J Menu\n",enddelay=2)
    questions=[
        inquirer.List(
            "Option",
            message="What would would you like to do?",
            choices=["Answer a math question for a point","Answer a rotation question for a point","Answer a logic question","Guess a number for a point","Quit"]
        )
    ]
    while True:
        answer: str=str(inquirer.prompt(questions)["Option"])
        OptionsDict[answer]()

Menu()



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
