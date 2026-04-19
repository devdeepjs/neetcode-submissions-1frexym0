class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l= 0
        count_s1 = [0]*26
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')]+=1

        count_s2 = [0]*26
        for r in range(len(s2)):
            count_s2[ord(s2[r])-ord('a')]+=1
            if (r-l+1==len(s1)):
                if (count_s1==count_s2):
                    return True
                count_s2[ord(s2[l])-ord('a')]-=1
                l+=1
        return False            
        