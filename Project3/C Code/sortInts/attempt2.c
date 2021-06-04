
int* quickSort(int* array, int numsSize);

int* sortArray(int* nums, int numsSize, int* returnSize){
    quickSort(nums, numsSize);
    return 0;
}

int* quickSort(int* array, int numsSize){
    int* subarray1;
    int* subarray2;
    int subarray1Len = 0; 
    int subarray2Len = 0;
    int pivot;

    
    if (numsSize > 1){
        if (numsSize % 2 == 1){
            pivot = array[(numsSize-1) / 2]; 
        } else {
            pivot = array[(numsSize) / 2]; 
        }
        for (int i = 0; i < numsSize; i++){
            if (array[i] < pivot){
                *(subarray1+subarray1Len) = *(array+i);
                 subarray1Len +=1;
            }
            else{
                // *(subarray2+subarray2Len) = *(array+i);
                 subarray2Len +=1;
            }
        }
        quickSort(subarray1, subarray1Len);
        quickSort(subarray2, subarray2Len);
    }
    return 0;
    
}