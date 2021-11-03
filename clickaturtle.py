# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spotColor = "pink"
spotShape = "circle"
spotSize = 5
points = 0
#-----initialize turtle-----
spot = trtl.Turtle()
counter_one = trtl.Turtle()
counter =  trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.speed(0)
spot.penup()
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game functions--------
def spot_clicked(x,y):
  points = 0
  size = rand.randint(1, 10)
  change_position(size)
  points = points + 1
def change_position(size):
  points =+ 1
  Lives(points)
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  colors = ["blue" , "red", "green", "pink"]
  colorcycle = rand.randint(0,3)
  spot.hideturtle()
  spot.fillcolor(colors[colorcycle])
  spot.turtlesize(size)
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()
class Lives(trtl.Turtle):
  FONT = ("Arial", 24, "normal")
  def __init__(self, lives):
    super().__init__()
    self.lives = points
    self.color("red")
    self.hideturtle()
    self.penup()
    self.speed(0)
    self.goto(300, 300)
    self.gain_points()
  
  def gain_points(self):
    self.lives += 1
    self.clear()
    self.write("points: " + str(self.lives), font=self.FONT)

def countdown():
  global timer, timer_up
  counter.penup()
  counter.goto(-300, 300)
  counter.pendown()
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
