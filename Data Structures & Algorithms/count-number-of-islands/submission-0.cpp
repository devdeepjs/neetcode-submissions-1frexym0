class Solution {
public:
    int df[5] = {0,1,0,-1,0};
    void dfs(vector<vector<char>> &grid, int i , int j){
        if (grid[i][j]=='0'){
           return ;
        }
        grid[i][j]='0';
        for (int k=0;k<4;++k){
            int l = i + df[k];
            int r = j + df[k+1];
            if (l<0 || r <0 || l>=grid.size() || r>=grid[0].size()){
                continue;
            }
            dfs(grid,l,r);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0 ; 
        for (int i=0;i<grid.size();++i){
            for (int j=0;j<grid[0].size();++j){
                if (grid[i][j]=='1'){
                    count++;
                    dfs(grid,i,j);
                }
            }
        }
        return count;
    }
};
