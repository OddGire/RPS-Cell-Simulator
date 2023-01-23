# Import modules
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

maps = [map1.original, map2.original, map3.original, map4.original, map5.original]
map = random.choice(tuple(maps))
# Create a function to randomly load in a map
def loadMap():
  print(map)

loadMap()