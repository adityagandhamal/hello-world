from functools import reduce                                                          #to use lambda function

print("Enter the elements of the sequence")                                           #input from the user
list_of_nums = list(map(int,input().split()))                                         #user enters the numbers with spacing
print(f"input {list_of_nums}")           

result = []                                                                           #empty list

c = 0                                                                                 #initialization

for i in list_of_nums:                                                                #looping over given list of numbers from the user

    list_of_nums.remove(i)                                                            #removes the element for each iteration i
    r = reduce(lambda x,y:x*y,list_of_nums)                                           #anonymous function 
    result.append(r)                                                                  #returned value of lambda function is appended to the empty list
    list_of_nums.insert(c,i)                                                          #inserts the removed iteration i
    c += 1                                                                            #incrementation

print(f"output {result}")                                                             #final output answer
