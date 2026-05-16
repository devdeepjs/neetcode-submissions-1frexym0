class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for (int i=0;i<nums.size()-1;++i){
            if (nums[i]==nums[i+1]){
                nums[i] = 101;
            }
        }
        int l = 0 ; 
        int i = 0 ; 
        while(i<nums.size()){
            if (nums[i]!=101){
                swap(nums[l],nums[i]);
                l++;
            }
            i++;
        }
        return l;
    }
};