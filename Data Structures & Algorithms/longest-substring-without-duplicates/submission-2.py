class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0 
        index = 0 
        for i,v in enumerate(s):
            while ord(v)-ord('a') in seen:
                seen.remove(ord(s[index])-ord('a'))
                index+=1
            seen.add(ord(v)-ord('a'))
            ans = max(ans,i-index+1)
        return ans    


        