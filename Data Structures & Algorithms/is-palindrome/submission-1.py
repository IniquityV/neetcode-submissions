class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        return new_string[::-1] == new_string