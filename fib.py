n = int(input("Enter the length of the series: "))

print("The Fibonacci Series is: ")

a = 0
b = 1

print(a,end=" ")
print(b,end=" ")

for i in range(n-1):
    c = a + b
    a = b
    b = c
    print(c,end=" ")
