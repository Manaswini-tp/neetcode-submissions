class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for c in strs:
            key = "".join(sorted(c))
            if key in groups:
                groups[key].append(c)
            else:
                groups[key]=[c]
        return list(groups.values())
