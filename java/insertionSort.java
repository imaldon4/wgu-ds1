class insertionSort{
    public static void main(String[] args){
        int[] numbers = {10, 2, 78, 4, 45, 32, 7, 11};
        System.out.println("UNSORTED: ");
        for (int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i] + " ");
        }
        System.out.println();

        InsertionSort(numbers);

        System.out.println("SORTED: ");
        for (int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i]); 
        }
        System.out.println();
    }


    public static int[] InsertionSort(int[] numbers){
        int j = 0;
        int temp = 0;

        for (int i = 1; i < numbers.length; ++i){
            j = i;
            while (j > 0 && numbers[j] < numbers[j - 1]){
                temp = numbers[j];
                numbers[j] = numbers[j - 1];
                numbers[j - 1] = temp;
                --j; 
            }
        }
        return numbers;

    }
}

