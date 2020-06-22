import java.util.Arrays;

// ShellSort.java

public class ShellSort {
    public static void main(String[] args){
        

        int[] arr = {34, 24, 54, 12, 67, 3, 44, 89, 90, 65, 35, 28, 48, 
                    36, 17, 27, 36, 58, 69, 76, 24, 35, 67,6};

        int[] gapValuesListed = {5, 3, 1};
        shellSort(arr, gapValuesListed);
        
        System.out.println(Arrays.toString(arr));
    }

    public static void shellSort(int[] numList, int[] gapValues){
        InsertionSortInterleaved InsertionSortInt = new InsertionSortInterleaved();
        for (int gapValue : gapValues){
            for (int i = 0; i < gapValue; i++){
                InsertionSortInt.isi(numList, i , gapValue);
            }
        }
    }
}