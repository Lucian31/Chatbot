
from turtle import *
import time
turtle = Turtle()
screen = Screen()

screen.bgcolor("lightblue")
turtle.color("black")


def chatbox (x,y, length, message, t, c, type):

  def corner (tut):
    for i in range (4):
      tut.circle(-10,15)
    tut.right(30)

  t.pu()
  t.goto(x,y)
  t.pd()
  t.color(c)
  
  t.begin_fill()
  t.left(45)
  t.fd(30)
  t.left(45)
  t.fd(30)
  corner(t)
  t.fd(length)
  corner(t)
  t.fd(30)
  corner(t)
  t.fd(length)
  t.lt(30)
  t.fd(35)
  t.ht()
  t.end_fill()
 
  if type == 1:
    t.pu()
    t.goto(x+30,y+40)
    t.pd()
    t.color("black") 
    t.write(message, font = ("Arial", 10, "bold"))
  elif type == -1:
    t.pu()
    t.goto(x-length-30,y-40)
    t.pd()
    t.color("black") 
    t.write(message, font = ("Arial", 10, "bold"))


turtle.speed(100)
quesHiName = "  Hi! My name is Ioana. What is your name?"


chatbox(-280, 150, 300, quesHiName , turtle, "white", 1)


print("Tell me your name ! ")
name = input()

turtle.setheading(0)
turtle.left(180)
nameMessage = "Hi! My name is " + name + " . "
chatbox(200, 170, 250, nameMessage, turtle, "lightgreen",-1)


turtle.setheading(0)
quesClass = "What is your age " + name +"?"
chatbox(-280, 40, 300, quesClass, turtle, "white",1)



study = input("enter your age : ")

studyMessage = "  My age is " + study + " . "
turtle.setheading(0)
turtle.left(180)
chatbox(200, 40, 150, studyMessage, turtle, "lightgreen",-1)

turtle.setheading(0)
quesSubject = "Which subject do you like?" 
chatbox(-280, -70,200, quesSubject, turtle, "white",1)



subject = input("enter your subject : ") 

subjectMessage = "  I love " + subject + " ! "
turtle.setheading(0)
turtle.left(180)
chatbox(200, -50, 160, subjectMessage, turtle, "lightgreen",-1)

turtle.setheading(0)
nameTagMessage = "I would like to make a Name Tag for you. Please wait..."
chatbox(-280, -200, 400, nameTagMessage, turtle, "white",1)


time.sleep(3)
turtle.reset()
turtle.speed(100)

turtle.pu()
turtle.goto(-150,150)
turtle.pd()
turtle.color("white")
nameTagMessage2 = "Here is your name tag :  "
turtle.write(nameTagMessage2, font = ("comic sans ms", 20, "normal"))
turtle.ht()
turtle.pu()
turtle.goto(-210,110)
turtle.pd()
turtle.color("lightgreen")
turtle.width(10)



turtle.forward(400)
turtle.right(90)
turtle.forward(190)
turtle.left(90)
turtle.backward(400)
turtle.left(90)
turtle.forward(190)



turtle.setheading(0)
turtle.pu()
turtle.goto(-190,90)
turtle.pd()


turtle.color("lightpink")
turtle.begin_fill()



turtle.forward(360)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.backward(360)
turtle.left(90)
turtle.forward(150)

turtle.end_fill()
turtle.setheading(0)

turtle.color("black")
turtle.pu()
turtle.goto(-180,55)
turtle.pd()

tagName = 'Name : ' + name 
turtle.write(tagName, font = ("comic sans ms", 20, "normal"))


turtle.pu()
turtle.goto(-160,45)
turtle.pd()
turtle.width(2)


turtle.forward(200)


turtle.forward(100)
turtle.pu()
turtle.goto(-180,10)
turtle.pd()


tagClass = 'Age : ' + study
turtle.write(tagClass, font = ("comic sans ms", 20, "normal"))


turtle.pu()
turtle.goto(-160, -5)
turtle.pd()
turtle.forward(300)

turtle.pu()
turtle.goto(-180,-40)
turtle.pd()

tagSubject = 'Subject : ' + subject
turtle.write(tagSubject, font = ("comic sans ms", 20, "normal"))


## Copyright © 2021 | Bujeniță Lucian-Andrei 