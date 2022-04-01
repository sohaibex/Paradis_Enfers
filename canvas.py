
import numpy as np
from numpy import random
from numpy import array
import sys
import time

if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
    
unit = 120
height = 4
width = 4
size_width = width*unit
size_height= height*unit

class Canvas(tk.Tk, object):
    def __init__(self):
       super(Canvas, self).__init__()
       self.title("Canvas")
       self.init()
        
    def init(self):

       self.canvas = tk.Canvas(
       self, bg='white', height=size_height, width=size_width)
       self.actions = ["left", "right", "top", "bottom"]

       #colone
       for c in range(width+1):
           x0, y0 = c * unit, 0
           x1, y1 = x0, y0 + height * unit
           self.canvas.create_line(x0, y0, x1, y1)
       #ligne
       for r in range(width+1):
           x0, y0 = 0, r*unit
           x1, y1 = x0 + width * unit, y0
           self.canvas.create_line(x0, y0, x1, y1)

       
       startPoint = np.array([unit/8, unit/8])

    
  #First trap HELL 3/2
       x0, y0 = startPoint[0] + (width - 2) * unit, startPoint[1] + (height - 3) * unit
  
       x1, y1 = x0 + 3 * unit / 4, y0 + 3 * unit / 4
      
       self.hell1 = self.canvas.create_rectangle(x0, y0, x1, y1, fill='black')
  #second trap HELL 2/3
       x0, y0 = startPoint[0] + (width - 3) * unit, startPoint[1] + (height - 2) * unit
       x1, y1 = x0 + 3 * unit / 4, y0 + 3 * unit / 4
       self.hell2 = self.canvas.create_rectangle(x0, y0, x1, y1, fill='black')      
        
       for i in range(6):
           for j in range(6):
               x0, y0 = startPoint[0]+j*unit, startPoint[1]+i*unit
               x1, y1 = x0+3*unit/4, y0+3*unit/4
               if i == 0 and j == 0:
                   #Agent
                   self.rect = self.canvas.create_rectangle(
                               x0, y0,
                               x1, y1,
                               fill='red')

               elif i == 2 and j == 2:
                   oval_center = startPoint + unit * 2
                   #Heaven 3/3
                   self.oval = self.canvas.create_oval(
                               x0, y0,
                               x1, y1,
                               fill='yellow')
       self.canvas.pack()
    
    def reintialize(self):
       self.update()
       time.sleep(0.5)
       self.canvas.delete(self.rect)
       startPoint = np.array([unit/8, unit/8])
       x0, y0 = startPoint[0]+0*unit, startPoint[1]+0*unit
       x1, y1 = x0+3*unit/4, y0+3*unit/4
       self.rect = self.canvas.create_rectangle(
           x0, y0,
           x1, y1,
           fill='red')
       return self.canvas.coords(self.rect)
    
    def random_move(self, action):
       
        cur_state = self.canvas.coords(self.rect)
        base_action = np.array([0,0])
        if action == 'top': # haut
            if cur_state[1] > unit:
                base_action[1] = base_action[1] - unit
        elif action == 'bottom': # bas
            if cur_state[1] < (height-1)*unit:
                base_action[1] = base_action[1] + unit
        elif action == 'right': # droite
            if cur_state[0] < (width-1)*unit:
                base_action[0] = base_action[0] + unit
        elif action == 'left': # gauche
            if cur_state[0] > unit:
                base_action[0] = base_action[0] - unit
                
        self.canvas.move(self.rect, base_action[0], base_action[1])
        next_move = self.canvas.coords(self.rect) 
        
        
        if next_move == self.canvas.coords(self.oval):
            reward = 1    
            over = True
            next_move = 'terminal'
           
            # print("Point gagne!")
        elif next_move == self.canvas.coords(self.hell1) or next_move == self.canvas.coords(self.hell2):
            reward = -1
            over = True
            next_move = 'terminal'
            # print("Point perdu!")
        else:
            reward = 0
            over = False
        return next_move, reward, over
    
    def render(self):
        time.sleep(0.1)
        self.update()
 
      
def update():
    for period in range(10):
        state = env.reintialize()
        while 1:
            env.render()
            act = 1
            state, reward, over = env.random_move(act)
            if over:
                break

if __name__ == "__main__":
    env = Canvas()
    env.after(100, update)
    env.mainloop()
