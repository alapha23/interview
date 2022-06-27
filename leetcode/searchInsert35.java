import java.util.Arrays;

class searchInsert35 {
	// THIS ATTEMPT FAILED
    public static int searchInsert(int[] nums, int target) {
	int len = nums.length;
	if(nums[len-1] == target) return len-1;
        if(nums[len-1] < target) return len;
	if(nums[0]>= target) return 0;
	int iter = len/2;
	System.out.println(iter);

	// even length. 1 3 5 7 cut in half, iter = 2
	if ((len % 2) == 0) {
	if (nums[iter] == target) {
	  return iter;
	}
	else if (nums[iter] > target) {
	  int []a = Arrays.copyOfRange(nums, 0, iter);
	  if (a.length == 2) {return iter-1;}
	  return searchInsert(a, target);
	} 
	else /*if (nums[iter] < target)*/ {
	  int []a = Arrays.copyOfRange(nums, iter, len);
	  if (a.length == 2) {return iter+1;}
          return iter+searchInsert(a, target);
	}
	}
        else {
		// odd. 1 3 5 7 9, iter = 2, num[2] = 5
        if (nums[iter] == target) {
          return iter;
        }
        else if (nums[iter] > target) {
          int []a = Arrays.copyOfRange(nums, 0, iter);
	  if (a.length == 1) return iter;
	  return searchInsert(a, target);
	} else /*if (nums[iter] < target)*/ {
          int []a = Arrays.copyOfRange(nums, iter, len);
          if (a.length == 2) {return iter+1;}
          return iter+searchInsert(a, target);
        }
    }
    }

    public static void main(String args[]) {
	int []nums = {3,4,9,10};
        System.out.println(searchInsert(nums, 5));
    }
}
