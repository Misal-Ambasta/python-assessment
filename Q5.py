# Write a one-line Python expression (no loops) that generates a list of all integers between 1 and 1000 that are:

# divisible by 7 or 9, but not both

# and are palindromic numbers (e.g., 121)


div = [s%7==0 or s%9==0 for s in range(1, 1000)]
# print(div)

def is_palindrome(num):
    return num[::-1] == num

print(is_palindrome('1214'))