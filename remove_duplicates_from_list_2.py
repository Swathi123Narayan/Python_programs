l1 = [11,22,1,1,4,1,5,2,5,6,7,8,9,9,11]
final_list = []
for item in l1:
    if item not in final_list:
        final_list.append(item)

print("the unique records are : ", final_list)