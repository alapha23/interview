import java.util.ArrayList;

public class RMElm27 {

    public static int[] removeDuplicates(int[] nums, int val) {
      //ArrayList<Integer> result = new ArrayList<Integer>();
      /*for (int i : nums) {
        if (result.contains(i)) {
        } else {
          result.add(i);
        }
      }*/
      //int []ret = result.stream().mapToInt(Integer::intValue).toArray();
      // 0 1 2 3 4 5 6 7 8 9
      // 0 0 1 1 1 2 2 3 3 4
      int finalLength = nums.length;
      for (int i =0; i < nums.length; i++) {
          if (i > finalLength - 1) {
	      break;
	  }
          if (nums[i] == val) {
                    finalLength--;
                    for (int k = i; k < nums.length-1; k++) {
                        nums[k] = nums[k+1];
                    }
		    i--;
          }
      }
      //return finalLength;
      System.out.println(finalLength);
      return nums;
    };

    public static void main(String []args) {
        //int []num = {3,5,2,3,6,1,2};
	int []num = {0,0,1,1,1,2,2,3,3,4};
	//int []num = {1,1};
	int []new_arr = removeDuplicates(num, 1);
	for (int elm : new_arr) {
  	  System.out.print(elm + " ");
	}
        System.out.println("");
    }
}
