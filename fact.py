n = int(input("Enter the length of AP: "))

def ap(n):
    a = int(input("Enter the first term of the AP: "))
    d = int(input("Enter the common difference of the AP: "))

    print("THE SEQUENCE IS:")

    print(a)

    for i in range(1,1+n):
        a+=d
        print(a)



