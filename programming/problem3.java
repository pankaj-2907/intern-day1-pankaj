import java.util.HashMap;

public class problem3{
    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 3, 1, 1};
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for (int num : nums) {
            if (freqMap.containsKey(num)) {
                freqMap.put(num, freqMap.get(num) + 1);
            }else{
                freqMap.put(num, 1);
            }
        }
        System.out.println("Frequency of elemnts in array: " + freqMap);
    }
}