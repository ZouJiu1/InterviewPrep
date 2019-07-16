#include<iostream> 
using namespace std;
//Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* n = new ListNode(0);
        ListNode* first = n;
        ListNode* curr = first;
        int x,y,sum;
        int pre = 0;
      	while (l1||l2){
      		if (l1){
      			x = l1->val;
      			l1 = l1->next;
			}
			else{
				x = 0;
			}
			if (l2){
				y = l2->val;
				l2 = l2->next;
			}
			else{
				y = 0;
			} 
      		sum=pre+x+y;
      		pre = sum/10;
      		ListNode* n = new ListNode(sum%10);
      		curr->next=n;
      		curr=curr->next;
		  }
		if (pre==1){
			ListNode* n = new ListNode(1);
			curr->next=n;
		}
		return first->next;
    }
};

int main(){
	ListNode* x1 = new ListNode(2);
	ListNode* x2 = new ListNode(4);
	x1->next = x2;
	ListNode* x3 = new ListNode(3);
	x2->next = x3;
	x3->next=NULL;
	
	ListNode* x4 = new ListNode(5);
	ListNode* x5 = new ListNode(6);
	x4->next = x5;
	ListNode* x6 = new ListNode(4);
	x5->next = x6;
	x6 ->next=NULL;
	
//	while (x4!=NULL){
//		cout<<x4->val<<"\t";
//		x4=x4->next;
//	}
	cout<<endl;
	Solution so = Solution();
	ListNode* x7 = new ListNode(0);
	x7 = so.addTwoNumbers(x1,x4); 
	
	while (x7!=NULL){
		cout<<x7->val<<endl;
		x7 = x7->next;
	}
	return 0;
}
