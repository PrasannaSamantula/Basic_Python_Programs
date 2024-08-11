# CHECK PALINDROME OR NOT

# STRINGS
str1 = input("Enter string:")
rev = str1[::-1]
if rev == str1:
    print("Palindrome")
else:
    print("Not Palindrome")

# LISTS
list1 = list(map(int,input("Enter numbers with comma:").split(",")))
lisrev = list1[::-1]
if  lisrev == list1:
    print("Palindrome")
else:
    print("Not Palindrome")

# EACH ITEM IN LIST IS PALINDROME OR NOT
def is_palindrome(s):
    # Checks if a string is a palindrome.
    return s == s[::-1]

def check_list_palindromes(lst):
    # Checks each element in a list for palindromes.
    for item in lst:
        if is_palindrome(str(item)):
            print(f"{item} - palindrome.")
        else:
            print(f"{item} - not a palindrome.")

# Example usage:
my_list = list(map(int,input("Enter numbers with comma:").split(",")))
check_list_palindromes(my_list)