public class problem1{
    public static void main(String[]args){
        int[] nums = {10, 5, 8, 10, 3};

        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for(int num : nums){
            if(num > largest){
                secondLargest = largest;
                largest = num;
            } else if(num > secondLargest && num != largest){
                secondLargest = num;
            }
        }
        System.out.println("The Second largest number is: " + secondLargest);
    }
}