import pandas as pd
import os
from read_csv import read_task
import numpy as np
from collections import deque
import ast

ones_list = []
def game(input_mat):
    input_mat = np.array(input_mat)
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    q = deque()
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
        
#Change the second input of this file to the path of the Task_Training_Data csv file
df = read_task("Task_Training_Data.csv", r"C:\Users\Pavan Nayak\Desktop\git-demo\ca2020demogit")


county = 0
breaker = False
while county <3:
    ask_name = str(input('What is your name?'))
    ask_email = str(input('what is your email?'))
    
    if ask_name in tuple(df['Name']) and ask_email in tuple(df['Email']):
        breaker = True
        break
    
    elif ask_name not in tuple(df['Name']) or ask_email not in tuple(df['Email']):
        county += 1
        print('Name or Email not recognized. You have ' + str(3-counter) + ' tries left.')
        

if county >= 3:
    print('you have entered incorrect information too many times. GoodBye.')
    

while breaker == True:
    print("Welcome to the brain game of Rivers and Land: Just Remember what you give")
    print("This game can make you happy or cause you copious amounts of stress.")
    
    ask_in = str(input("Do you want to get in and play the game (Y/N) ?"))
    
    if ask_in.upper() == 'N':
        breaker = False
        
    elif ask_in.upper() == 'Y':
        inp_mat = np.array(ast.literal_eval(input('Welcome to the River Game: Please input a matrix of 0s and 1s as a list of lists: ')))
        
        if type(inp_mat) == np.ndarray:
        
            ones_list = game(np.array(inp_mat))
            guess_size()
            breaker = False
        
        