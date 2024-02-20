package POC_Proof_Of_Concepts;

import java.util.Arrays;

class test{
    
    public static String[] arr = {"a", "b", "c", "d"};
    public static String[] shift(String[] arr){
        String last_elm = arr[arr.length - 1];
        String[] result = new String[arr.length];
        for(int i = 1; i < arr.length; i++){
            result[i] = arr[i - 1];
        }
        result[0] = last_elm;

        return result;
    }
    public static void main(String[] args){
        for(String each:shift(arr)){
            System.out.println(each);
        }
        String testing = "abcd";
        System.out.println(testing.substring(0, 1));

        int[] a = {1, 2, 3};
        int[] b = a; //{1, 2, 3};
        System.out.println(a.equals(b));
        System.out.println(Arrays.equals(a, b));;
    }
}
