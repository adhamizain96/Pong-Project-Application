#!/usr/bin/env python
# coding: utf-8

# In[2]:


import turtle as t
#constant is a type of variable whose value cannot be changed.
ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        #t.penup() - pull the pen up – no drawing when moving
        self.penup()
        #t.hideturtle() - make the turtle invisible
        self.hideturtle()
        #user 1
        self.l_score = 0
        #user 2
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        #t.goto() - Move turtle to an absolute position.
        self.goto(-100, 200)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self.goto(100, 200)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


# In[ ]:




