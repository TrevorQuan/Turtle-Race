import turtle
import random

# Functions: a group of related staments that perform a specific task
# Functions help us brea down a program into sections
# DRY: Don't Repeat Yourself
# Formula:
# def functionName (parameters):
#   BODY
#   optional 'return' statement

# BUILDERMAN

def drawtrack(length):
  Builder = turtle.Turtle()
  Builder.shape("triangle")
  Builder.speed(0)
  Builder.penup()
  Builder.goto(-175, 140)

  for i in range(length):
    Builder.write(i)
    Builder.right(90)
    Builder.forward(20)
    Builder.pendown()
    Builder.forward(200)
    Builder.left(180)
    Builder.penup()
    Builder.forward(220)
    Builder.right(90)
    Builder.forward(20)
  Builder.hideturtle()


# CONTESTANTS
supabob = turtle.Turtle()
turboltle = turtle.Turtle()
DaEpicTurtle = turtle.Turtle()
ShellShot = turtle.Turtle()
SpeedrunTortoise = turtle.Turtle()
def createTurtles():
  supabob.shape("turtle")
  supabob.penup()
  supabob.goto(-200, 100)
  supabob.color("yellow green")

  turboltle.shape("turtle")
  turboltle.penup()
  turboltle.goto(-200, 60)
  turboltle.color("gold")

  DaEpicTurtle.shape("turtle")
  DaEpicTurtle.penup()
  DaEpicTurtle.goto(-200, 20)
  DaEpicTurtle.color("green")

  ShellShot.shape("turtle")
  ShellShot.penup()
  ShellShot.goto(-200, -20)
  ShellShot.color("red")

  SpeedrunTortoise.shape("turtle")
  SpeedrunTortoise.penup()
  SpeedrunTortoise.goto(-200, -60)
  SpeedrunTortoise.color("purple")


# GOGOGO

def startrace():
  for i in range(40):
    supabob.forward(random.randint(1,15))
    turboltle.forward(random.randint(1,15))
    DaEpicTurtle.forward(random.randint(1,15))
    ShellShot.forward(random.randint(1,15))
    SpeedrunTortoise.forward(random.randint(1,15))

drawtrack(16) # function call
createTurtles()
startrace()