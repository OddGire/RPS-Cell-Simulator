import tkinter as tk
# from PIL import ImageTk, Image
playPressed = False
settingsPressed = False

window = tk.Tk()
window.title("Rock, Paper, Scissors Cell Simulator")
window.geometry("300x300")

hello = tk.Label(text="Rock, Paper, Scissors Cell Simulator")
hello.pack()
play = tk.Button(text="Play", command=playPressed)
play.pack()
settings = tk.Button(text="Settings", command=settingsPressed)
settings.pack()
# img = ImageTk.PhotoImage(Image.open("image.jpg"))

if playPressed:
  bg = 'red'
  
if settingsPressed:
  settingsPressed = True

# if playPressed:
#   window.configure(bg='red')
tk.mainloop()

# Import
import random

# Create board class
class Board:
  def __init__(background, original, rock, paper, scissors):
    background.original = original
    background.rock = rock
    background.paper = paper
    background.scissors = scissors
map1 = Board(1,2,3,4)
map2 = Board(5,6,7,8)
map3 = Board(9,10,11,12)
map4 = Board(13,14,15,16)
map5 = Board(17,18,19,20)

maps = [map1, map2, map3, map4, map5]
map = random.choice(tuple(maps))
# Create a function to randomly load in a map
def loadMap():
  print(map)

# loadMap()