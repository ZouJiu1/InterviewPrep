#include<iostream>
#include<string> 
#include<map>

using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> tmpmap;
        int left =0;
        int length = 0;
        for (int i=0;i<s.size();i++){
        	cout<<s.at(i)<<endl;
        	if (tmpmap.count(s[i])==0|tmpmap[s[i]]<left){
        		length = max(length, i - left +1);
			}
			else{
				left = tmpmap[s[i]];
			}
			tmpmap[s[i]]=i+1;
		}
		return length;
    }
};
int main(){
	string s("abcabcbb");
	cout<<s.size()<<endl;
	cout<<s[1]<<endl; 
	Solution so = Solution();
	cout<<so.lengthOfLongestSubstring(s);
	return 0;
}
