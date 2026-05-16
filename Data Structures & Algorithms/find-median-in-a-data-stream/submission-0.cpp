class MedianFinder {
public:
        priority_queue<int> small;
        priority_queue<int,vector<int>,greater<int>> large;

    MedianFinder() {
    }
    
    void addNum(int num) {
        small.push(num);
        large.push(small.top());
        small.pop();
        // this ensures the <= condition 
        if (large.size()>small.size()+1){
            small.push(large.top());
            large.pop();
        }
    }
    
    double findMedian() {
        if ((small.size() + large.size())%2){
            return large.top();
        }
        return (small.top() + large.top()) / 2.0;
    }
};
