class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 1e5 
        l , r = 1 , sum(piles)
        while(l<=r):
           m = l + (r-l)//2
           sum_h = 0
           for i in piles:
            sum_h+=(i//m) + (1 if i%m else 0)
           if (sum_h<=h):
              ans = m 
              r = m -1 
           else : 
              l = m+1      
        return ans     
        