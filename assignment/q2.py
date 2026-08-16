#2) Write a Python program to implement the Tower of Hanoi problem using a user-defined recursive function. 
# The number of rings will be user input. The output will show all the steps to solve the problem.  
# Sample User Input  Enter the number of rings: 3
# Expected Output 
# Steps to solve the Tower of Hanoi: 
# Move Disk 1 from A to C
# Move Disk 2 from A to B
# Move Disk 1 from C to B
# Move Disk 3 from A to C
# Move Disk 1 from B to A
# Move Disk 2 from B to C
# Move Disk 1 from A to C
# Total number of moves = 7




def toh(num,start,aux,end):
    if num==1:
     print("Move disk 1 from {} to rod {}".format(start,end))
     return
    toh(num-1,start,end,aux)    #Move the smaller disks from A → B
    print("Move disk {} from {} to rod {}".format(num,start,end))  #Move the biggest disk from A → C
    toh(num-1,aux,start,end)  #Move the smaller disks from B → C
disc=2
toh(disc,"A","B","C")  
