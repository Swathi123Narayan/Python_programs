num = int(input("enter the number to be checked: "))
prime = True
#prime number : the number which is divisible by 1 and itself is called prime 
#for ex: 1, 2 , 3, 5, 7, 11 etc
for i in range(2, num):
    if (num==2):
        prime = True
    elif num % i == 0 :
        prime = False
        break
if prime:
    print(f"the given {num} is a prime number")
else:
    print(f"the given number {num} is not a prime number")
