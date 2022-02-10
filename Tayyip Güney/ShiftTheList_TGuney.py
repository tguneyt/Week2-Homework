"""
Tayyip GÜNEY - 06.02.2022
Shift The List

Write a program that takes two inputs; one of them is a list 
and the other is a number, and returns the list obtained by 
shifting the elements in the list n places to the right (left) 
when n is positive (negative). Use wrap-around if an element is 
shifted beyond the end of the list, then continue to shift starting 
at the beginning of the list. Example Inputs [1, 2, 3, 4, 5], 2 Output 
[4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]
"""

length=int(input("How many members will you enter for shifting ? "))

list=[input(f"Enter the {i+1}. element : ") for i in range(length)] #fill the list
y=int(input("\nEnter number for change. for right(+)/left(-) : "))

print("\nMain list : ",list)

if y>0:     # Shift right
    list[0:0] = list[-y:]     # take after -y index, add to first index and shift the remaining indexes
    del list[-y:]             # delete after -y index 
else:       # Shift left
    list.extend(list[0:-y])   # (-y) is positive because y is negative 
    del list[0:(-y)]  
print("\nNew List  : ",list)    
