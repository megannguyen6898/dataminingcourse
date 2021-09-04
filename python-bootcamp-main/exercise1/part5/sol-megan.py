#O is obstacle
#A is answer for the path
#G is the goal
#U is open, unchecked
#C is checked, visited

import csv

with open('Kelvin Maze.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    Maze = list(csv_reader)

Sol = Maze
#Initialize x and y
for r in range(len(Maze)):
    if 'S' in Maze[r]:
        startx = r
        starty = Maze[r].index('S')
#Find path


def find_path(x, y):
    if Maze[x][y] == 'O':
        return False
    if Maze[x][y] == 'C':
        return False
    if Maze[x][y] == 'G':
        print(x,y)
        return True
    Maze[x][y] = 'C'
    if find_path(x+1, y):       #prioritises down-up search before right-left
        print(x,y)
        Sol[x][y] = 'A'
        return True
    if find_path(x-1, y):
        print(x,y)
        Sol[x][y] = 'A'
        return True
    if find_path(x, y+1):
        print(x,y)
        Sol[x][y] = 'A'
        return True
    if find_path(x, y-1):
        print(x,y)
        Sol[x][y] = 'A'
        return True


find_path(startx, starty)

with open('Megan-Sol.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(Sol)