// QuickSort
public class QuickSort{

    // Access starts here
    public static void quickSort(int[] array){
        int lowIndex = 0;
        int highIndex = array.length - 1;
        quickSort(array, lowIndex, highIndex);
    }

    private static void quickSort(int[] numArray, int lowIndex, int highIndex){
        if (lowIndex >= highIndex){
            return;
        }

        int lowEndIndex = partition(numArray, lowIndex, highIndex);
        quickSort(numArray, lowIndex, lowEndIndex);
        quickSort(numArray, lowEndIndex + 1, highIndex);    
    }

    private static int partition(int[] numArray, int lowIndex, int highIndex) {
        return 0;
    }

}