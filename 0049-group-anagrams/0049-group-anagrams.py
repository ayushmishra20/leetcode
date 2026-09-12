class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char = {}
        
        for i in strs:
            key = "".join(sorted(i))

            if key not in char:
                char[key] = []

            char[key].append(i)

        return list(char.values())