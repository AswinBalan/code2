import turtle
import os
import math
import random
from tkinter import messagebox
import pygame


sob =turtle.Screen()
sob.bgcolor("white")
sob.title("Game")
sob.bgpic("sp2.gif")

turtle.register_shape("p6.gif")
turtle.register_shape("p8.gif")

b=turtle.Turtle()
b.speed(0)
b.color("black")
b.penup()
b.setposition(-300,-300)
b.pendown()
b.pensize(3)
for side in range(4):
    b.fd(600)
    b.lt(90)
b.hideturtle()


score =0

score_pen =turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestr ="Score: %s" %score
score_pen.write(scorestr, False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()



player=turtle.Turtle()
player.color("red")
player.shape("p8.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15



no_enemy = 10

enemies =[]

for i in range(no_enemy):

    enemies.append(turtle.Turtle())

for enemy in enemies:
    #enemy =turtle.Turtle()
    enemy.color("green")
    enemy.shape("p6.gif")
    enemy.penup()
    enemy.speed(0)
    x =random.randint(-200, 200)
    y =random.randint(100, 250)
    enemy.setposition(x,y)

    enemyspeed = 3

#player weapon
wp =turtle.Turtle()
wp.color("red")
wp.shape("triangle")
wp.penup()
wp.speed(0)
wp.setheading(90)
wp.shapesize(0.5,0.5)
wp.hideturtle()


wp_speed = 20

wp_state ="ready"

def move_left():
    x = player.xcor()
    x -=playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x =player.xcor()
    x +=playerspeed
    if x > 280:
        x =280
    player.setx(x)


def fire_bul():
       global wp_state
    #if wp_state == "ready":
        
       file = 'shoot.wav'
       pygame.init()
       pygame.mixer.init()
       pygame.mixer.music.load(file)
       pygame.mixer.music.play()
       wp_state = "fire"
       x=player.xcor()
       y=player.ycor() +10
       wp.setposition(x,y)
       wp.showturtle()


def isCollision(t1, t2):
     distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
     if distance < 15 :
        return True
     else:
        return False
#create keyword bindings

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bul,"space")

while True:
  for enemy in enemies:
    #move the enemy
    x =enemy.xcor()
    x +=enemyspeed
    enemy.setx(x)

    #reverse enemy
    if enemy.xcor() > 280:
        for e in enemies:
           y =e.ycor()
           y -= 40
           e.sety(y)
        enemyspeed *= -1   
          
    if enemy.xcor() < -280:
        for e in enemies:
           y =e.ycor()
           y -= 40
           e.sety(y)
        enemyspeed *= -1
        
    if isCollision(wp, enemy):
        fi = 'invaderkilled.wav'
        #pygame.init()
        #pygame.mixer.init()
        pygame.mixer.music.load(fi)
        pygame.mixer.music.play()
       #reset the bullet
        wp.hideturtle()
        wp_state = "ready"
        wp.setposition(0, -400)
       #reset the enemy
        x =random.randint(-200, 200)
        y =random.randint(100, 250)
        enemy.setposition(x,y)
        #updating score
        score +=10
        scorestr="Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestr, False, align="left", font=("Arial",14,"normal"))

    if isCollision(player, enemy):
        fil = 'invaderkilled.wav'
        pygame.init()
        #pygame.mixer.init()
        pygame.mixer.music.load(fil)
        pygame.mixer.music.play()
        player.hideturtle()
        sc =[]
        j=0
        sc.append(score)
        for i in sc:
            if score < i:
                j +=1
        
        if j == 0:
            messagebox.showinfo("congrats","HIGH SCORE")
        result = messagebox.askyesno()
        if result == True:
            exec('./space-invader.py').read()
        else:
            messagebox.showwarning("GAMEOVER")
        break

        
  if wp_state == "fire":
       y = wp.ycor()
       y += wp_speed
       wp.sety(y)

  if wp.ycor() > 275:
       wp.hideturtle()
       wp_state ="ready"

                         

delay =input("enter")
