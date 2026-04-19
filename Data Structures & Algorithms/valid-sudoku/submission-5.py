class Solution:
    def isDup(nums: List[str]):
        n = len(nums)
        count = [0]*(n+1)
        for i in range(n):
            if (nums[i]=="."):
                continue
            count[int(nums[i])]+=1
            if (count[int(nums[i])]>1):
                return True
        return False 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            if (Solution.isDup(board[i])):
                return False

        for i in range(n):
            if (Solution.isDup([board[j][i] for j in range(n)])):
                return False

     # 3x3 boxes using center cell idea
        for i in range(1, n, n//3):
            for j in range(1, n, n//3):
                arr = [
                    board[i][j],
                    board[i+1][j+1], board[i-1][j-1],
                    board[i-1][j+1], board[i+1][j-1],
                    board[i+1][j], board[i-1][j],
                    board[i][j-1], board[i][j+1]
                ]
                if Solution.isDup(arr):
                    return False

        return True            
                    

        