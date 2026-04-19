class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pq = []
        for v,c in count.items():
            heapq.heappush(pq,(-c,v))
        ans = []
        for _ in range(k):
            c,v = heapq.heappop(pq)
            ans.append(v)
        return ans    


        