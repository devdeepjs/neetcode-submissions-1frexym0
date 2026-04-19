class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        count = [0]*26
        left = 0 
        for i in range(len(s)):
            count[ord(s[i])-ord('A')]+=1
            sum = 10000
            index = 0
            while(left<i and k<sum-count[index]):
                index = 0 
                sum = 0
                for j in range(26):
                    sum+=count[j]
                    if (count[j]>count[index]):
                        index = j
                if (k>=sum-count[index]):
                    break
                else :
                    count[ord(s[left])-ord('A')]-=1
                    left+=1
            ans = max(i - left+1,ans)
        return ans                        


