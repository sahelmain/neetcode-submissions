class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for character in s:
             if character.isalnum():
                new_string += character.lower()
        return new_string == new_string[::-1]