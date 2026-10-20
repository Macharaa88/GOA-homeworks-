from turtle import *

#we want to paint house
speed(100)

width(7)
color("brown")

begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()
<<<<<<< HEAD:homework/lesson1.py

=======
>>>>>>> bcb4f3ae8939d7b8a39042aab90af05fa6faf753:lesson1.py
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 175)
pendown()
#windows
begin_fill()
color("blue")
left(30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(130, 175)
pendown()

begin_fill()
color("blue")
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


exitonclick()
