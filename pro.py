from functools import reduce

print("Enter the elements of the sequence")
list_of_nums = list(map(int,input().split()))
print(f"Your list: {list_of_nums}")

result = []

c = 0

for i in list_of_nums:

    list_of_nums.remove(i)
    r = reduce(lambda x,y:x*y,list_of_nums)
    result.append(r)
    list_of_nums.insert(c,i)
    c+=1

print(f"Your answer: {result}")
