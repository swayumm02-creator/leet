class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
            
        return list(anagrams.values())