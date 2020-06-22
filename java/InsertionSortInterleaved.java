public class InsertionSortInterleaved {
    
    public int[] isi(int[] numList, int startIndex, int gap){
        for (int i = startIndex + gap; i < numList.length; i = i + gap){
            int j = i;
            while (j - gap >= startIndex && numList[j] < numList[j - gap]){
                int temp = numList[j];
                numList[j - gap] = numList[j];
                numList[j - gap] = temp;
                j = j - gap;
            }
        }

        return numList;
    }
}