#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t

class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        #t.shapesize() - return or set the pen’s attributes x/y - stretchfactors and/or outline
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        #t.penup() - pull the pen up - no drawing when moving.
        self.penup()
        #t.goto() - move turtle to an absolute position
        #t.goto() - go_up(self)/go_down(self)
        self.goto(position)
    def go_up(self):
        y_new = self.ycor() + 20
        self.goto(self.xcor(), y_new)
    def go_down(self):
        y_new = self.ycor() - 20
        self.goto(self.xcor(), y_new)


# In[ ]:




