class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t)>len(s)):
            return ""

        count_s , count_t = defaultdict(int),defaultdict(int)
        for i in range(len(t)):
            count_s[s[i]]+=1
            count_t[t[i]]+=1
        
        matches = 0 
        for i in count_t:
            if (count_t[i]<=count_s[i]):
                matches+=1 
        desired_match_count=len(count_t.keys())

        ans = [-1,100000]
        l , i  = 0 , len(t)
        while(l<i):
            print(ans,matches,l,i)
            while l<i and matches==desired_match_count:
                ans = [l,i-1] if i-l <= ans[1]-ans[0] else ans
                count_s[s[l]]-=1
                if count_t[s[l]]>0 and count_s[s[l]]<count_t[s[l]]:
                    print(ans,matches,l,i)
                    matches-=1
                l+=1

            if (i<len(s)):    
                count_s[s[i]]+=1
                if count_t[s[i]]>0 and count_s[s[i]]==count_t[s[i]]:
                    matches+=1 
                i+=1    
            else : 
                l+=1
    
        return s[ans[0]:ans[1]+1]  if ans[0]!=-1 else ""                 








        