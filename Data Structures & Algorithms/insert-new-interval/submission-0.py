class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        in_hand = intervals[0]
        for i in range(1,len(intervals)):
            invt = intervals[i]
            if (in_hand[1]<invt[0]):
                ans.append(in_hand)
                in_hand = invt
            else : 
                in_hand[0] = min(in_hand[0],invt[0])
                in_hand[1] = max(in_hand[1],invt[1])
        ans.append(in_hand)
        return ans           



        