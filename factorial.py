num = int(input("enter the number: "))
fact = 1
# for i in range(1,num+1):
#     fact = fact*i

for i in range(num):
    fact = fact+(fact*i)


print(f"the factorial of the given number {num} is : ", fact)