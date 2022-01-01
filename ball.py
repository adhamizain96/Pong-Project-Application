#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_pos_new = 3
        self.y_pos_new = 3
        self.move_speed = 0.1
    def move(self):
        x_new = self.xcor() + self.x_pos_new
        y_new = self.ycor() + self.y_pos_new
        self.goto(x_new, y_new)
    def x_bouce(self):
        self.x_pos_new *= -1
        self.move_speed *= 0.9
    def y_bounce(self):
        self.y_pos_new *= -1
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        slef.x_bounce()


# In[ ]:




