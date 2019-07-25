#include<iostream>
#include<string> 
#include<vector>
using namespace std; 
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length()<=1){
                return s;
        }
        int sizes = s.length();
        int cur_len = 1;
        int longest_l = 1;
        string res = s.substr(0,1);
        vector<vector<bool> > dp(sizes,vector<bool>(sizes,false));
        for(int r=1;r<sizes;r++){
            for(int l=0;l<r;l++){
                if ((s[l]==s[r])&((r-l<=2)|(dp[l+1][r-1]))){
                    dp[l][r] = true;
                    cur_len = r-l+1;
                    if (cur_len>longest_l){
                        longest_l = cur_len;
                        res = s.substr(l, r-l+1);
                    }
                }
            }
        }
        return res;
    }
};

int main(void){
	string strs = "babad";
	Solution s = Solution();
	string r =s.longestPalindrome(strs);
	cout<<r<<endl;
	return 0;
}
