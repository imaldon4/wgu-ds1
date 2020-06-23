public class InsertionSortComparable{
    public static void insertionSort(Comparable[] array){

        for (int unsortedIndex = 1; unsortedIndex < array.length; unsortedIndex++){
            Comparable unsortedElement = array[unsortedIndex];
            int lowestSortedIndex = 0;
            int highestSortedIndex = unsortedIndex - 1;

            while (highestSortedIndex >= lowestSortedIndex && unsortedElement.compareTo(array[highestSortedIndex]) < 0){
                array[highestSortedIndex + 1] = array[highestSortedIndex]; // Make room
                highestSortedIndex--;
            }
            array[highestSortedIndex +1] = unsortedElement;
        }
    }

}