str = "TacoCat"
str = str.casefold()
revStr = reversed(str)

str1 = "Pancake"
str1 = str1.casefold()
revStr1 = reversed(str1)

if list(str) == list(revStr):
    print(str, "is a palindrome.")
else:
    print(str, "is not a palindrome")

if list(str1) == list(revStr1):
    print(str1, "is a palindrome.")
else:
    print(str1, "is not a palindrome.")