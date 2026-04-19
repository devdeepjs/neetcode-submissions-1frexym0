class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0 
        left = 0 
        for i in range(len(s)):
            while left<i and s[i] in seen:
                seen.remove(s[left])
                left+=1
            ans = max(i-left+1,ans)
            seen.add(s[i])
        return ans    
            


        