class Solution {
public:
int df[5] = {0,1,0,-1,0};

    int dfs(vector<vector<int>> &grid, int i , int j){
        if (grid[i][j]==0){
           return 0;
        }
        grid[i][j]=0;
        int sum = 0 ; 
        for (int k=0;k<4;++k){
            int l = i + df[k];
            int r = j + df[k+1];
            if (l<0 || r <0 || l>=grid.size() || r>=grid[0].size()){
                continue;
            }
            sum+=dfs(grid,l,r);
        }
        return sum+1;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
                int count = 0 ; 
        for (int i=0;i<grid.size();++i){
            for (int j=0;j<grid[0].size();++j){
                if (grid[i][j]==1){
                    count = max(count,dfs(grid,i,j));
                }
            }
        }
        return count;
    }
};
