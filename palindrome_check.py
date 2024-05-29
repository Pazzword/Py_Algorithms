# For words
def is_palindrome(s):
    return s == s[::-1]

example = "Anzor"

print(is_palindrome(example))


# For numbers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]