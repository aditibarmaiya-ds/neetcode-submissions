from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       anagrams = {} 
       for j in range(len(strs)):
        word = strs[j]
        count = [0]*26

        for i in range(len(word)):
            ch = word[i]
            ind = ord(ch) - ord('a')
            count[ind] += 1
        key = tuple(count)
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
       result=list(anagrams.values())
       return(result)     