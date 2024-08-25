l1= [10,40,50,60,30,20,100,409,49]
largest = l1[0]

for i in range(len(l1)):
    if l1[i]>largest:
        largest=l1[i]

print("the largest of the given list is : ", largest)