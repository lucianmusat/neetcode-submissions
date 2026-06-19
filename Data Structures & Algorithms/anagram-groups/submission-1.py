class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def base_anagram(s: str) -> str:
            return ''.join(sorted(s))

        anagrams = {}
        for word in strs:
            base_ang = base_anagram(word)
            if base_ang in anagrams:
                anagrams[base_ang].append(word)
            else:
                anagrams[base_ang] = [word]
        return list(anagrams.values())