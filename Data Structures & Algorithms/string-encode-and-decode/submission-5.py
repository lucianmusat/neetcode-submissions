class Solution:

    def encode(self, strs: List[str]) -> str:
        # Use a list to efficiently build the encoded string
        encoded = []
        for word in strs:
            encoded.append(f"{len(word)}#{word}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the length of the next word
            j = s.find("#", i)  # Find the next '#'
            word_len = int(s[i:j])  # Get the number before '#'
            i = j + 1  # Move past the '#'
            
            # Extract the word of length `word_len`
            word = s[i:i + word_len]
            res.append(word)
            
            # Move past the current word
            i += word_len
        return res
