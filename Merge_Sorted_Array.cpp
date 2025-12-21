class Solution {
public:
    vector<int> mergedArray;
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
       
        for (int i=0;i<m;i++){
           // while(nums1[i+1]!=0){                
                mergedArray.push_back(nums1[i]);
           // }
        }
          for (int j = 0;j<n;j++){
            mergedArray.push_back(nums2[j]);
        } 
        sort(mergedArray.begin(),mergedArray.end());    
        nums1 = mergedArray;  
    }
    
};
