class TimeMap:

    def __init__(self):
       self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.mp[key])==0:
            return ""

        l, r = 0, len(self.mp[key])-1
        ans = ""
        while(l<=r):
            mid =  l + (r-l)//2
            if (self.mp[key][mid][0]<=timestamp):
                ans = self.mp[key][mid][1]
                l = mid + 1
            else : 
                r = mid-1
        return ans        
                
        
