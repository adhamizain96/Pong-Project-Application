#!/usr/bin/env python
# coding: utf-8

# In[3]:


import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white') 
        self.shape('circle')
        #t.penup() - pull the pen up - no drawing when moving
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        #t.goto() - move turtle to an absolute position
        self.goto(x_new, y_new)
    def x_bounce(self):
        #operator - *= - x *= 5 -> x = x * 5
        self.x_move *= -1
        self.move_speed *= 0.9
    def y_bounce(self):
        self.y_move *= -1
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()


# In[ ]:




