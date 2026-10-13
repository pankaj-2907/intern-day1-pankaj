public class problem2 {
    public static void main(String[] args) {
        String str = "madam";
        boolean isPalindrome = true;

        int left = 0;
        int right = str.length() -1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }
        System.out.println("The string: " + str + " is palindrome = " + isPalindrome);
    }
}
