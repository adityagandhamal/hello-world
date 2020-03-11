print("ARITHEMATIC PROGRESSION")

n = int(input("Enter the length of AP: "))   #for user to enter the length of the AP  

def ap(n):                                   #defines function for AP  
    a = int(input("Enter the first term of the AP: "))                 #for user to enter first term of the AP
    d = int(input("Enter the common difference of the AP: "))          #for user to enter the common difference of the AP

    print("THE SEQUENCE IS:")                                          

    print(a,end = " ")                            #prints the first term

    for i in range(1,1+n):              #code for AP
        a+=d
        print(a,end = " ")
        
ap(n)                               #calling the function


