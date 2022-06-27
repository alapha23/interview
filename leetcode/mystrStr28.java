
class mystrStr28 {

  public static int strStr(String haystack, String needle) {
    if (needle == "" || haystack == "") {
       return -1;
    }
    if (haystack.contains(needle)) {
       return haystack.indexOf(needle);
    } else return -1;
  }

  public static void main(String args[]) {
	 // System.out.println(strStr("hello", "ll"));
  System.out.println(strStr("aaaaa", "ll"));

  }
}
