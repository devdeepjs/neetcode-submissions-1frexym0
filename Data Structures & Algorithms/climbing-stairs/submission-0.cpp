class Solution {
public:
    int climbStairs(int n) {
        int x = 1 , y = 1 ; 
        for (int i=0;i<n-1;++i){
            int t  = x ; 
            x = x + y ; 
            y = t ; 
        }
        return x;
    }
};
