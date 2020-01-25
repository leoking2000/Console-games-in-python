import os
import mazegame.maze as maze

rows = 37
coloms = 57


os.system('mode con: cols='+str(coloms + 60)+'lines='+str(rows + 7))
mazeObj = maze.MAZE(rows,coloms)

maze.game(mazeObj)  


