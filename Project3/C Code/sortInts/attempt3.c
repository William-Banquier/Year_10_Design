int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
int* sortArray(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    int *returnValues = malloc(*(returnSize) * sizeof(int));

    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    for (int i = 0; i < numsSize; i++){
        *(returnValues+i) = *(nums+i);
    }

    return returnValues;
}
