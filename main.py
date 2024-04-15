import ris
import ras

board = ris.Chess()
queens = ras.Queen()
colors = ['red', 'blue']

for i in range(8):
    for j in range(8):
        if queens.brd[i][j]==1:
            board.Ferz(-200 + i * 50, -200 + j * 50, colors[(i+j)%2])

board.mainloop()