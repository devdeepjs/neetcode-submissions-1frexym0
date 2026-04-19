class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        count = [0]*26
        left = 0 
        maxf = 0
        for i in range(len(s)):
            count[ord(s[i])-ord('A')]+=1
            maxf = max(maxf,count[ord(s[i])-ord('A')])
            while(k<(i-left+1)-maxf):
                count[ord(s[left])-ord('A')]-=1
                left+=1
            ans = max(i - left+1,ans)
        return ans                        


