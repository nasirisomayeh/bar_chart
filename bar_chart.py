# نمودار میله ای

from turtle import width
import matplotlib.pyplot as nem

x = [1, 2, 3, 4, 5, 6]
y = [20, 40, 30, 10, 25, 35]

nem.bar(x,y,tick_label=["yek", "do", "se", "chahar", "panj", "shesh"],
        color=["blue" , "pink", "yellow", "green", "orange", "red"], 
        width=0.5)

nem.show()