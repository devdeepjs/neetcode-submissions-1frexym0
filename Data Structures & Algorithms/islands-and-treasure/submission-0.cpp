class Solution {
public:
    
    int df[5] = {0,1,0,-1,0};
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<pair<int,int>> q ; 
        for (int i=0;i<grid.size();++i){
            for (int j=0;j<grid[0].size();++j){
                if (grid[i][j]==0){
                    q.push({i,j});
                }
            }
        }

        while(!q.empty()){
            pair<int,int> top = q.front() ;
            q.pop();
            for (int i=0;i<4;++i){
                int l = top.first + df[i];
                int r = top.second + df[i+1];
                if (l<0 || r<0 || l>=grid.size() || r>=grid[0].size()
                || grid[l][r]!=INT_MAX){
                    continue;
                }
                grid[l][r] = grid[top.first][top.second] + 1 ;
                q.push({l,r});
            }
        }

    }
};
