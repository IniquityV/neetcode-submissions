class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        for word in strs:
            encoded_word += str(len(word)) + "$" + word 

        return encoded_word   


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            str_length = ""
            while s[i] != "$":
                str_length += s[i]
                i += 1
            word_length = int(str_length)
            start = i + 1
            end = start + word_length
            result.append(s[start:end])
            i = end
        return result
