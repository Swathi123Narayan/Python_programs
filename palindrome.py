str = input("enter the string : ")
rev_str = str[::-1]
if rev_str==str:
    print(f"the given string {str} is a palindrome")
else:
    print(f"the given string {str} is not a palindrome")