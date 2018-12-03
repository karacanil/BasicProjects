import time

# Starting the timer
start_time = time.time()

# Inserting the sudokus in a 9x9 form
#Example1
inp = [[0,0,0,2,0,0,0,0,9],
       [0,0,0,0,9,0,0,3,6],
       [0,0,0,0,0,5,1,4,0],
       [0,3,0,0,4,6,8,7,0],
       [1,0,0,0,2,0,0,0,3],
       [0,7,2,3,5,0,0,1,0],
       [0,2,5,8,0,0,0,0,0],
       [9,4,0,0,1,0,0,0,0],
       [6,0,0,0,0,4,0,0,0]]

#Example2
inp2 = [[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]]


def solver(grid, r=0, c=0):
    r,c = nextCell(grid, r ,c) # r stands for row, c stands for column

    if r == -1 or c == -1: # Checking if program run out of unprocessed cells
        # Terminating the process
        return True
    for num in range(1,10):
        if iscorrect(grid, r, c, num):
            grid[r][c] = num # Assigning the correct value to the certain cell
            if solver(grid, r, c): # Checking if all the values are valid and proper by calling the function again
                '''
                for i in grid:
                    print(i)
                print('\n\n\n')
                '''
                return True
            grid[r][c] = 0
    return False

def nextCell(grid, r, c):

    # Determining a cell to process
    for i in range(9):
        for k in range(9):
            if grid[i][k] == 0:
                return i,k

    # Returning -1,-1 for the if statement on the 33th line to terminate the program
    return -1,-1

def iscorrect(grid, r, c, num):
    topleftr = 3*(r//3) #Determining the r of the top left element
    topleftc = 3*(c//3) #Determining the c of the top left element


    if all([num != grid[r][i] for i in range(9)]): #Checking the row
        if all([num != grid[k][c] for k in range(9)]): #Checking the column

            #Checking the 3x3 grid
            for i in range(topleftr,topleftr+3):
                for k in range(topleftc,topleftc+3):
                    if grid[i][k] == num:
                        return False
            return True
    return False

'''
for i in inp:
    print(i)
solver(inp)
print(3*('\n'))
for i in inp:
    print(i)
'''
for i in inp2:
    print(i)
solver(inp2)
print(2*('\n'))
for i in inp2:
    print(i)

print('\n\nIt took %s seconds to solve that sudoku'%(time.time() - start_time))
