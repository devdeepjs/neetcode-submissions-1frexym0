class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = (len(A) + len(B)) 
        half = total//2

        if (len(B)<len(A)):
            A,B = B,A

        l , r = 0 , len(A)-1
        while True:
            mid = l + (r-l)//2
            m = half - mid -2 

            Aleft = A[mid] if mid>=0 else float("-infinity")
            Bleft = B[m] if m>=0 else float("-infinity")
            Aright = A[mid+1] if mid+1<len(A) else float("infinity")
            Bright = B[m+1] if m+1<len(B) else float("inifitiy")

            if (Aleft<=Bright and Bleft<=Aright):
                if total%2:
                    return min(Bright,Aright)
                else : 
                    return (min(Bright,Aright) + max(Aleft,Bleft))/2
            elif (Aleft > Bright):
                r = mid-1
            else : 
                l = mid+1
        return -1             


        