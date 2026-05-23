class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_string = cleaned_string.lower()
        length = len(cleaned_string)
        if len(cleaned_string)%2:
            first = cleaned_string[:int((length-1)/2)]
            last = cleaned_string[int((length+1)/2):]
            last = last[::-1]
            print(first,last)
            if first == last:
                return True
            else:
                return False
        else:
            first = cleaned_string[:int(length/2)]
            last = cleaned_string[int(length/2):]
            last = last[::-1]
            print(first,last)
            if first == last:
                return True
            else:
                return False