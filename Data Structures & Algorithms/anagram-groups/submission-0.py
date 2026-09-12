from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            key = str(sorted(s))
            if key in dictionary:
                dictionary[key].append(s)
            else:
                dictionary[key] = [s]
        return list(dictionary.values())

            

        