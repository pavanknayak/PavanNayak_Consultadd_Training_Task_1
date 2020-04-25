import numpy as np
from collections import deque

matrix = np.array([[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]])

ones_list = []
directions = [[1,0],[0,1],[-1,0],[0,-1]]
q = deque()

def game(input_mat):
    
    for i in range(0, len(input_mat)):
        for j in range(0, input_mat.shape[1]):
            
            if input_mat[i][j] == 1:
                input_mat[i][j] = 0
                q.append((i,j))
                riv_len = 0
                riv_len += 1
                while len(q) > 0:
                    qpop = q.pop()
                    trial_row = qpop[0]
                    trial_col = qpop[1]
                    for k in range(0, len(directions)):
                        
                        trial_row1 = trial_row + directions[k][0]
                        trial_col1 = trial_col + directions[k][1]
                        
                        if 0 <= trial_row1 < len(input_mat) and 0 <= trial_col1 < input_mat.shape[1]:
                            if input_mat[trial_row1][trial_col1] == 1:
                                input_mat[trial_row1][trial_col1] = 0
                                q.append((trial_row1, trial_col1))
                                riv_len += 1
                            
                            
                    
                ones_list.append(riv_len)
                riv_len = 0
                
    ones_list.sort()
    return ones_list
                            
                        
                        
                        
                        

def guess_size():
    
    guess_list = []
     
    for i in range(0, len(ones_list)):
        
        ask = input('Guess the size of River ' + str(i) + ':')
        guess_list.append(int(ask))
        
    correct_count = 0
    
    for j in range(0, len(guess_list)):
        
        if guess_list[j] in ones_list:
            correct_count += 1
            
        
    if correct_count < 0.6*len(ones_list):
        print("Invest more money on Almonds, then come back")
        
    elif 0.6*len(ones_list) <= correct_count < len(ones_list):
        print("you got second position")
        
    elif correct_count == len(ones_list):
        print("You are the winner")
        

ones_list = game(matrix)
guess_size()

    