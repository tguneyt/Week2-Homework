"""
Tayyip GÜNEY - 07.02.2022
Compare Two Words

Write a program that takes in two words as input and returns a list containing three elements, 
in the following order Shared letters between two words. Letters unique to word 1. Letters unique to word 2. 
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. 
The strings will always be in lowercase and will not contain any punctuation. 
Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']
"""

a=set(input("Please enter the first word\n"))
b=set(input("Please enter the second word\n"))

list_fs=[list(a.difference(b)),list(b.difference(a)),list(a & b)] #make a new list for sets
list_result=[]         # final list for result

for k in list_fs:
    var_w=""        # variable as string for the list 
    k.sort()        # to sort a list within list_fs 
    for m in k:     
        var_w=var_w+m # to concatenate data as string
    list_result.append(var_w) 
    
print(list_result)