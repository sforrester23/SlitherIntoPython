# This is a recursive function that takes a string as an argument and returns whether or not that string is a palindrome
def isPalindrome(str):
    l = len(str)
    if l<=1:
        return True
    if str[0]==str[-1]:
        return isPalindrome(str[1:-1])
    return False

print(isPalindrome('racecar'))
print(isPalindrome('incombob'))       
print(isPalindrome('saras'))
        