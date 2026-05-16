class MedianFinder {
public:
    priority_queue<int> left; 
    priority_queue<int,vector<int>,greater<int>> right;

    MedianFinder() {
        
    }
    
    void addNum(int num) {
        right.push(num);
        left.push(right.top());
        right.pop();
        
        if (left.size()-right.size()>1){
            right.push(left.top());
            left.pop();
        }
    }
    
    double findMedian() {
        if ((left.size() + right.size())%2){
            return left.top();
        }
        return (left.top() + right.top()) / 2.0;
    }
};
