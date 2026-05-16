class Solution {
public:
   int df[5] = {0,1,0,-1,0};

    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int,int>> q ; 
        for (int i=0;i<grid.size();++i){
            for (int j=0;j<grid[0].size();++j){
                if (grid[i][j]==2){
                    q.push({i,j});
                }
            }
        }
        
        int ans = -1 ; 
        while(!q.empty()){
            int n = q.size();
            ans++;
            for (int k=0;k<n;++k){
            pair<int,int> top = q.front() ;
            q.pop();
            for (int i=0;i<4;++i){
                int l = top.first + df[i];
                int r = top.second + df[i+1];
                if (l<0 || r<0 || l>=grid.size() || r>=grid[0].size()
                || grid[l][r]!=1){
                    continue;
                }
                grid[l][r] = 2 ; 
                q.push({l,r});
            }
            }
        }

        for (int i=0;i<grid.size();++i){
            for (int j=0;j<grid[0].size();++j){
                if (grid[i][j]==1){
                    return -1;
                }
            }
        }

        return max(ans,0);
    }
};
