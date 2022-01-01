#!/usr/bin/env python
# coding: utf-8

# In[3]:


import turtle as t
ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self.goto(100,200)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


# In[ ]:



