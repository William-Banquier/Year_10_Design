// Solution Failed Because of time constraints
//[5,3,2,1] -> [1,2,3,5]
int* sortArray(int* nums, int numsSize, int* returnSize){
    int i, j, t;
   
    // printf(**returnSize);
    *returnSize = numsSize;
    int *returnValues = malloc(*(returnSize) * sizeof(int));
    
    //Basic brute force sort
    //Loops though all numbers
    for (i = 0; i < numsSize; i++){
        //Second Loop
        for(j = i + 1; j < numsSize; j++){
            if(*(nums+j) < *(nums+i)){
                t = *(nums + i);
                *(nums+i) = *(nums+j);
                *(nums+j) = t;
            }
        }
    }

    for (int i = 0; i < numsSize; i++){
        *(returnValues+i) = *(nums+i);
    }


    return returnValues;
}

//int *list -> [0,1,2,3]
//*(list+0) -> 0
//*(list+1) -> 1
//*(list+2) -> 2
//*(list+3) -> 3
