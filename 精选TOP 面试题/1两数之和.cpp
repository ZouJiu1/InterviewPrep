#include<iostream>
#include<vector>
#include<map>
using namespace std;
//class Solution {
//public:
//    vector<int> twoSum(vector<int>& nums, int target) {
//    	vector<int> result;
//		for (int j=0; j<nums.size();j++){
//			for (int i =j+1;i<nums.size();i++) {
//				if ((nums[j]+nums[i])==target){
//					result.push_back(j);
//					result.push_back(i);
//					return result;
//				}
//			}
//		}
//		return {};
//    }
//};
//class Solution {
//public:
//    vector<int> twoSum(vector<int>& nums, int target) {
//    	vector<int> result;
//    	map<int, int> tmpmap;
//    	for (int j=0; j<nums.size();j++){
//    		tmpmap[nums[j]] = j;
//		}
//		for (int j=0; j<nums.size();j++){
//			if (tmpmap.count(target-nums[j])!=0&&tmpmap[target-nums[j]]!=j){
//				result.push_back(j);
//				result.push_back(tmpmap[target-nums[j]]);
//                return result;
//			}
//		}
//		return {};
//    }
//};
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	vector<int> result;
    	int half = target/2;
    	map<int, int> tmpmap;
		for (int j=0; j<nums.size();j++){
            if (nums[j]==half&&tmpmap.count(target-nums[j])!=0){
                result.push_back(tmpmap[target-nums[j]]);
                result.push_back(j);
                return result;
            }
            tmpmap[nums[j]]=j;
			if (tmpmap.count(target-nums[j])!=0&&tmpmap[target-nums[j]]!=j){
                if (j>tmpmap[target-nums[j]]){
                    result.push_back(tmpmap[target-nums[j]]);
                    result.push_back(j);
                    return result;
                }
			}
		}
		return {};
    }
};
int main(){
	vector<int> a ;
	vector<int> vec;
	int x[] = {3,3};
	int target = 6;
	a.insert(a.begin(), x, x+2);
	Solution so = Solution();
	vec = so.twoSum(a, target);
	for (int i = 0; i<vec.size();i++){
		cout<<vec[i];
	}
	return 0;
}
