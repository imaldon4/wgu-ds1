import java.util.Arrays;

// ShellSort.java

public class ShellSort {
    public static void main(String[] args) {

        int[] arr = { 34, 24, 54, 12, 67, 3, 44, 89, 90, 65, 35, 28, 48, 36, 17, 27, 36, 58, 69, 76, 24, 35, 67, 6 };

        int[] gapValuesListed = { 5, 3, 1 };
        shellSort(arr, gapValuesListed);

        System.out.println(Arrays.toString(arr));
    }

    public static void shellSort(int[] numList, int[] gapValues) {
        for (int gapValue : gapValues) {
            for (int i = 0; i < gapValue; i++) {
                insertionSortInterleaved(numList, i, gapValue);
            }
        }
    }

    public static void insertionSortInterleaved(int[] numList, int startIndex, int gap) {
        for (int i = startIndex + gap; i < numList.length; i = i + gap) {
            int j = i;
            while ((j - gap >= startIndex) && (numList[j] < numList[j - gap])) {
                int temp = numList[j];
                numList[j] = numList[j - gap];
                numList[j - gap] = temp;
                j = j - gap;
            }
        }
    }
}