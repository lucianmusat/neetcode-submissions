class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def base_anagram(s: str) -> str:
            return ''.join(sorted(s))

        anagrams = {}
        for _str in strs:
            base_ang = base_anagram(_str)
            if base_ang in anagrams:
                anagrams[base_ang].append(_str)
            else:
                anagrams[base_ang] = [_str]
        return [anagram_list for anagram_list in anagrams.values()]