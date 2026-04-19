
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            v = [0]*26
            for c in s:
                v[ord(c)-ord('a')]+=1;
            res[tuple(v)].append(s)
        return list(res.values())       

