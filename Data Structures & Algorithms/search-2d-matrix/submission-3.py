class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix),len(matrix[0])
        l , r = 0, rows - 1 
        while(l<=r):
            m = l + (r-l)//2 
            if (matrix[m][-1]<target):
                 l = m+1
            elif (matrix[m][0]>target):
                 r = m-1
            else : 
               break     

        if not (l<=r):
            return False

        i = (l+r)//2
        l , r = 0 , cols-1
        while l<=r:
            m = l + (r-l)//2
            if (matrix[i][m]<target):
                l = m+1
            elif (matrix[i][m]>target):
                r = m-1
            else : 
                return True

        return False                        


        