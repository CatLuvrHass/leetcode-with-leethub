class Solution {
    public int minSetSize(int[] arr) {
        
        /*
        Using a map to record frequency 
        Add to a Queue in decreasing order
        
        Subtract them one by one from the size of the original array,
        Record the number of steps.
        
        **/
        
        Map<Integer, Integer> freqMap = new HashMap<>();
        PriorityQueue<Integer> countVal = new PriorityQueue<>(Comparator.reverseOrder());
        
        for (int num: arr) freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        for (int val: freqMap.values()) countVal.offer(val);
        
        int size = arr.length; int result = 0;
        while (size > arr.length / 2) {
            size -= countVal.poll();
            result++;
        }
        return result;
    }
}