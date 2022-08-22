class Solution {
    public double average(int[] salary) {
        double min = Double.MAX_VALUE; 
        double max = Double.MIN_VALUE;
        double sum = 0; 
        for (double i: salary){
            sum += i;
            if(i > max) max = i;
            if(i < min) min = i;
        }
     return (sum - max - min)/(salary.length - 2);   
    }
}