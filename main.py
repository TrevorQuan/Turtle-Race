import turtle
import random

# BUILDERMAN

Builder = turtle.Turtle()
Builder.shape("triangle")
Builder.speed(0)
Builder.penup()
Builder.goto(-175, 140)

for i in range(16):
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
supabob.shape("turtle")
supabob.penup()
supabob.goto(-200, 100)
supabob.color("yellow green")
turboltle = turtle.Turtle()
turboltle.shape("turtle")
turboltle.penup()
turboltle.goto(-200, 60)
turboltle.color("gold")
DaEpicTurtle = turtle.Turtle()
DaEpicTurtle.shape("turtle")
DaEpicTurtle.penup()
DaEpicTurtle.goto(-200, 20)
DaEpicTurtle.color("green")
ShellShot = turtle.Turtle()
ShellShot.shape("turtle")
ShellShot.penup()
ShellShot.goto(-200, -20)
ShellShot.color("red")
SpeedrunTortoise = turtle.Turtle()
SpeedrunTortoise.shape("turtle")
SpeedrunTortoise.penup()
SpeedrunTortoise.goto(-200, -60)
SpeedrunTortoise.color("purple")

# GOGOGO

for i in range(40):
  supabob.forward(random.randint(1,15))
  turboltle.forward(random.randint(1,15))
  DaEpicTurtle.forward(random.randint(1,15))
  ShellShot.forward(random.randint(1,15))
  SpeedrunTortoise.forward(random.randint(1,15))