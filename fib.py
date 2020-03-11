n = int(input("Enter the length of the series: "))   #for user to input length of the fibonacci series

print("The Fibonacci Series is: ")                   

a = 0                                               '''first term and second terms of the fibonacci series'''
b = 1

print(a,end=" ")                                    #prints first and second terms
print(b,end=" ")

for i in range(n-1):                                #looping over the length provided by the user
    c = a + b                                       #third variable which is the next term of the fibonacci series
    a = b                                           '''value of a is assigned to b,'''
    b = c                                           '''and value of b is assigned to c'''
    print(c,end=" ")                                #prints value of c and the loop continues
