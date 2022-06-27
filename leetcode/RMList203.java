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
    public ListNode removeElements(ListNode head, int val) {
        ListNode n = head;
	// check head null
	if (n == null)
		return head;
	// check body
        while(n.next!=null) {
            if (n.next.val == val) {
                n.next = n.next.next;
            }
	    else {
                n = n.next;
	    }
        }
	// check head val finally
	if (head.val == val) {
           if (head.next != null)
		   return head.next;
	   else return null;
	}
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

public class RMList203 {
   public static void main(String []args) {
     Solution s = new Solution();
     ListNode head = new ListNode(1);
     ListNode cursor = head;
     for (int i = 2; i < 7; i++) {
       ListNode n = new ListNode(i);
       cursor.next = n;
       cursor = n;
     }
     cursor = head;
     while (cursor != null) {
       System.out.println(cursor.val);
       cursor = cursor.next;
     }
     s.removeElements(head, 6);
     cursor = head;
     while (cursor != null) {
       System.out.println(cursor.val);
       cursor = cursor.next;
     }
   }
}
