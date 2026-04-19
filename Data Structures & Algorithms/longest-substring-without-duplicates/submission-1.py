class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = [0]*256
        ans = 0 
        index = 0 
        for i,v in enumerate(s):
            while count[ord(v)-ord('a')]>0:
                count[ord(s[index])-ord('a')]-=1
                index+=1
            count[ord(v)-ord('a')]+=1
            ans = max(ans,i-index+1)
        return ans    


        