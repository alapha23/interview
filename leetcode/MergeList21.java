/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
	ListNode head = null;
	ListNode cursor = null;
        ListNode cur1 = l1;
        ListNode cur2 = l2;
	if (cur1 == null) return l2;
	if (cur2 == null) return l1;
	while (cur2 != null || cur1 != null) {
/*ListNode tmp = cur1;
     while (tmp != null) {
       System.out.print(tmp.val);
       tmp = tmp.next;
     } 
     System.out.println("");*/
            if (cur1 == null) {
	        cursor.next = cur2;
		cur2 = null;
	    }
	    else if (cur2 == null) {
		cursor.next = cur1;
		cur1 = null;
	    }
            else if (cursor == null) {
	        if (cur1.val < cur2.val) {
                  // insert cur1
                  cursor = cur1;
                  cur1 = cur1.next;
                }
                else {
                  // insert cur2
                  cursor = cur2;
                  cur2 = cur2.next;
                }
		head = cursor;
	    }
	    else if (cur1.val < cur2.val) {
                // insert cur1
	        cursor.next = cur1;
                cursor = cursor.next;
                cur1 = cur1.next;
	    }
	    else {
		// insert cur2
                cursor.next = cur2;
                cursor = cursor.next;
                cur2 = cur2.next;
	    }
	}
ListNode tmp = head;
     while (tmp != null) {
       System.out.print(tmp.val);
       tmp = tmp.next;
     } 
     System.out.println("");

        return head;
    }
}


class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class MergeList21 {

    public static void main(String []args) {
        Solution s = new Solution();
     ListNode head = new ListNode(1);
     ListNode cursor = head;
     for (int i = 2; i < 7; i++) {
       ListNode n = new ListNode(i);
       cursor.next = n;
       cursor = n;
     }
     cursor.next=null;
     cursor = head;
     while (cursor != null) {
       System.out.println(cursor.val);
       cursor = cursor.next;
     }
     
     ListNode head2 = new ListNode(1);
     ListNode cursor2 = head2;
     for (int i = 2; i < 7; i++) {
       ListNode n = new ListNode(i);
       cursor2.next = n;
       cursor2 = n;
     }
     cursor2.next=null;
     cursor2 = head2;
     while (cursor2 != null) {
       System.out.println(cursor2.val);
       cursor2 = cursor2.next;
     }

     cursor  = s.mergeTwoLists(head, head2);

     while (cursor != null) {
       System.out.println(cursor.val);
       cursor = cursor.next;
     } 
   }
}
