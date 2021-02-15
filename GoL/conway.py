"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]


def findShapes(grid,N):
    names = ["Block: ","Beehive: ","Loaf: ","Boat: ","Tub: ","Blinker: ","Toad: ","Beacon: ","Glider: ","Spaceship: "]
    shapes = np.zeros(10)
    porcent = np.zeros(10)
    visited = np.zeros(N*N).reshape(N, N)
    for x in range(1,N-1):
         for y in range(1,N-1):
            if(visited[x,y]==0):
                if(grid[x,y]==ON):
                    if(x<N-3 and y<N-3):
                        #Beehive
                        if(grid[x,y+1]==ON and grid[x+1,y-1]==ON and grid[x+1,y+2]==ON and grid[x+2,y]==ON and grid[x+2,y+1]==ON): 
                            shapes[1]+=1
                            visited[x,y+1]=1 
                            visited[x+1,y-1]=1 
                            visited[x+1,y+2]=1
                            visited[x+2,y]=1
                            visited[x+2,y+1]=1
                            visited[x,y]=1
                        #Boat
                        if(grid[x,y-1]==ON and grid[x+1,y-1]==ON and grid[x+1,y+1]==ON and grid[x+2,y]==ON ): 
                            shapes[3]+=1
                            visited[x,y-1]=1 
                            visited[x+1,y-1]=1
                            visited[x+1,y+1]=1 
                            visited[x+2,y]=1
                            visited[x,y]=1
                        #Tub
                        if(grid[x+1,y-1]==ON and grid[x+1,y+1]==ON and grid[x+2,y]==ON ): 
                            shapes[4]+=1
                            visited[x+1,y-1]=1
                            visited[x+1,y+1]=1 
                            visited[x+2,y]=1
                            visited[x,y]=1
                        #Toad 1
                        if(grid[x+1,y-2]==ON and grid[x+1,y+1]==ON and grid[x+2,y-2]==ON and grid[x+2,y+1] and grid[x+3,y-1] ): 
                            shapes[6]+=1
                            visited[x+1,y-2]=1 
                            visited[x+1,y+1]=1
                            visited[x+2,y-2]=1 
                            visited[x+2,y+1]=1
                            visited[x+3,y-1]=1
                            visited[x,y]=1
                        #Toad 2
                        if(grid[x,y+1]==ON and grid[x,y+2]==ON and grid[x+1,y-1]==ON and grid[x+1,y] and grid[x+1,y+2] ): 
                            shapes[6]+=1
                            visited[x,y+1]=1 
                            visited[x,y+2]=1
                            visited[x+1,y-1]=1 
                            visited[x+1,y]=1
                            visited[x+1,y+2]=1
                            visited[x,y]=1
                        #Glider 1
                        if(grid[x+1,y+1]==ON and grid[x+2,y-1]==ON and grid[x+2,y]==ON and grid[x+2,y+1] ): 
                            shapes[8]+=1
                            visited[x+2,y-1]=1 
                            visited[x+1,y+1]=1
                            visited[x+2,y]=1 
                            visited[x+2,y+1]=1
                            visited[x,y]=1
                         #Glider 2
                        if(grid[x,y+2]==ON and grid[x+1,y+1]==ON and grid[x+1,y+2]==ON and grid[x+2,y+1] ): 
                            shapes[8]+=1
                            visited[x,y+2]=1 
                            visited[x+1,y+1]=1
                            visited[x+1,y+2]=1 
                            visited[x+2,y+1]=1
                            visited[x,y]=1
                        #Glider 3
                        if(grid[x+1,y]==ON and grid[x+1,y-2]==ON and grid[x+2,y]==ON and grid[x+2,y-1] ): 
                            shapes[8]+=1
                            visited[x+1,y]=1 
                            visited[x+1,y-2]=1
                            visited[x+2,y]=1 
                            visited[x+2,y-1]=1
                            visited[x,y]=1
                        #Glider 4
                        if(grid[x+1,y+1]==ON and grid[x+1,y+2]==ON and grid[x+2,y]==ON and grid[x+2,y+1] ): 
                            shapes[8]+=1
                            visited[x+2,y]=1 
                            visited[x+1,y+1]=1
                            visited[x+1,y+2]=1 
                            visited[x+2,y+1]=1
                            visited[x,y]=1
                        #Beacon 
                        if(x<N-4 and y< N-4):
                        #Loaf
                            if(grid[x,y+1]==ON and grid[x+1,y-1]==ON and grid[x+1,y+2]==ON and grid[x+2,y]==ON and grid[x+2,y+2]==ON and  grid[x+3,y+1]==ON): 
                                shapes[2]+=1
                                visited[x,y+1]=1 
                                visited[x+1,y-1]=1 
                                visited[x+1,y+2]=1
                                visited[x+2,y]=1
                                visited[x+2,y+2]=1
                                visited[x+3,y+1]=1
                                visited[x,y]=1
                            if(grid[x,y+1]==ON and grid[x+1,y+1]==ON and grid[x+1,y]==ON and grid[x+2,y+2]==ON and grid[x+2,y+3]==ON and grid[x+3,y+2]==ON and grid[x+3,y+3]==ON):
                                shapes[7]+=1
                                visited[x+1,y+1]=1 
                                visited[x,y+1]=1 
                                visited[x+1,y]=1
                                visited[x+2,y+2]=1
                                visited[x+2,y+3]=1 
                                visited[x+3,y+2]=1 
                                visited[x+3,y+3]=1
                                visited[x,y]=1

                            if(grid[x,y+1]==ON ==ON and grid[x+1,y]==ON and grid[x+2,y+3]==ON and grid[x+3,y+2]==ON and grid[x+3,y+3]==ON):
                                shapes[7]+=1
                                visited[x,y+1]=1 
                                visited[x+1,y]=1
                                visited[x+2,y+3]=1 
                                visited[x+3,y+2]=1 
                                visited[x+3,y+3]=1
                                visited[x,y]=1

                        #Block
                        if(grid[x-1,y-1]==ON and grid[x,y-1]==ON and grid[x-1,y]==ON):
                            shapes[0]+=1
                            visited[x-1,y-1]=1 
                            visited[x,y-1]=1 
                            visited[x-1,y]=1
                            visited[x,y]=1
                        #Blinker 1
                        if(grid[x-1,y]==ON and grid[x+1,y]==ON):
                            shapes[5]+=1
                            visited[x-1,y]=1 
                            visited[x+1,y]=1
                            visited[x,y]=1
                        #Blinker 2
                        if(grid[x,y-1]==ON and grid[x,y+1]==ON):
                            shapes[5]+=1
                            visited[x,y-1]=1 
                            visited[x,y+1]=1
                            visited[x,y]=1
    pp = np.sum(shapes)
    for x in range(0,10):
        porcent[x] = str(round((shapes[x]/pp), 2))
    for x in range(0,10):
        #print(names[x]+shapes[x]+" porcentage: "+porcent[x] )
        print(names[x]+str(shapes[x])+ " porcentage: " + str(porcent[x]))

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    # glider = np.array([[0,    0, 255], 
    #                    [255,  0, 255], 
    #                    [0,  255, 255]])
    glider = np.array([[0,  255, 0,0], 
                       [255,  0, 255,0], 
                       [0,  255,   0,0],
                       [0,  0,   0,0]])
    grid[i:i+4, j:j+4] = glider

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    # print(grid)

    newGrid = grid.copy()

    # print("")
    # print(newGrid)
    # reglas del juego 
    for x in range(1,N-1):
        for y in range(1,N-1):
            sum = 0
            sum = grid[x-1,y-1] + grid[x-1,y] + grid[x-1,y+1] + grid[x,y-1] + grid[x,y+1] + grid[x+1,y-1] + grid[x+1,y] + grid[x+1,y+1]  
            sum /= 255
            if(grid[x,y]==ON):
                if(sum>=2 and sum<=3):
                    pass
                else:
                    newGrid[x,y] = OFF
            else:
                if(sum == 3):
                    newGrid[x,y] = ON
            # print(str(x)+" "+str(y)+" "+str(sum))

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    findShapes(grid,N)
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    
    # set grid size
    N = int(input())
        
    # set animation update interval
    updateInterval = 1000

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    # grid = np.zeros(N*N).reshape(N, N)
    # addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), frames = 5, interval=updateInterval, save_count=2)

    plt.show()

# call main
if __name__ == '__main__':
    main()