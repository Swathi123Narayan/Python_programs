l1 = [10,5,40,6,43]
l2 = [90,6,43,23]
new_list = []
for item in l1: 
    if item in l2:
        new_list.append(item)

print("the common values are : ", new_list)