class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_string = cleaned_string.lower()
        length = len(cleaned_string)
        if len(cleaned_string)%2:
            if cleaned_string[:int((length-1)/2)][::-1] == cleaned_string[int((length+1)/2):]:
                return True
            else:
                return False
        else:
            if cleaned_string[:int(length/2)][::-1] == cleaned_string[int(length/2):]:
                return True
            else:
                return False