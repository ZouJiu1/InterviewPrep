#encoding = utf-8
#include <cstdio>
#include <vector>
#include<iostream>
using namespace std;
//int INTMIN = 0x80000000;
//int INTMAX = 0x7FFFFFFF;
#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b)) 
class Solution {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int n = nums1.size();
		int m = nums2.size();
		
		//��֤����1һ�����
		if (n > m){
			return findMedianSortedArrays(nums2, nums1);
		}
		// Ci Ϊ��i������ĸ�,����C1Ϊ2ʱ��ʾ��1������ֻ��2��Ԫ�ء�LMaxiΪ��i�����������Ԫ�ء�RMiniΪ��i�����������Ԫ�ء�
		//����Ŀǰ���������'#'��������1��2*n����
		int LMax1, LMax2, RMin1, RMin2, c1, c2, lo = 0, hi = 2 * n;  
		//����
		while (lo <= hi){   
			c1 = (lo + hi) / 2;  //c1�Ƕ��ֵĽ��
			c2 = m + n - c1;

			LMax1 = (c1 == 0) ? INT_MIN : nums1[(c1 - 1) / 2];
			RMin1 = (c1 == 2 * n) ? INT_MAX : nums1[c1 / 2];
			LMax2 = (c2 == 0) ? INT_MIN : nums2[(c2 - 1) / 2];
			RMin2 = (c2 == 2 * m) ? INT_MAX : nums2[c2 / 2];

			if (LMax1 > RMin2)
				hi = c1 - 1;
			else if (LMax2 > RMin1)
				lo = c1 + 1;
			else
				break;
		}
		return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2.0;
	}
};


int main(int argc, char *argv[])
{
	
	vector<int> nums1 ;
	vector<int> nums2 ;
	vector<int> vec;
	int x[] = {2,7,11,15};
	nums1.insert(nums1.begin(), x, x+4);
	int w[] = { 1,4,7, 9 };
	nums2.insert(nums2.begin(), w, w+4);
		
	Solution solution;
	double ret = solution.findMedianSortedArrays(nums1, nums2);
	cout<<ret<<endl;
	return 0;
}
