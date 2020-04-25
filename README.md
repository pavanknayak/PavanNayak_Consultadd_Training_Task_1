# PavanNayak_Consultadd_Training_Task_1
River and Land Minor Project


Consultadd minor project game for counting the number and length of rivers (sequential 1s) in a given 2D matrix of 0s and 1s

How it works: Briefly, the program iterates through rows and columns of the matrix, and upon reaching a 1, changes it to a 0, and adds the index to a queue list. It then checks for any surrounding 1s to this index within the boundaries of the matrix. If a surrounding 1 exists, this 1 is changed to a 0, and the new index added to the queue list, and a counter keeps track of the length of 1s. This process is repeated as long as there is a value in the queue list. Once an index is reached where no 1s exist surrounding it, no index is added to the queue list, and the loop breaks, appending the counter to a list. The list is then output once no 1s exist in the matrix.

Read_csv and authenticate_data files place a backend logic of login and some questions to ask the user if they want to play the game.

