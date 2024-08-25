list1 = [1,2,1,5,110,4,2,2,4,5,10,6,2,10,1]
num = input("enter the numbers seperated by space: ")
list1 = list(map(int, num.split()))
frequency = {}
for i in list1:
    if i in frequency:
        frequency[i] = frequency[i]+1

    else:
        frequency[i]=1

print("the frequency of the numbers are displayed as below: ", frequency)
# print(f"the frequency of number 2 is {frequency[2]}")

# 2 3 4 2 3 4 5 6 3 12 7 8 3
# {2: 2, 3: 4, 4: 2, 5: 1, 6: 1, 12: 1, 7: 1, 8: 1}



