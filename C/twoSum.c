#include <stdio.h>

int main(){
    int array[] = {1,3,5,6,11,23};
    const int sum = 9;
    int target = sum;
    int result[2];
    for (int i = 0; i<sizeof(array)/sizeof(array[0]); i++){ //iterate first value through array
        if (target >= array[i]) { //if the element fits target
            target -= array[i]; //remove amount from target, that is the new target now
            result[0] = array[i]; //state that this amount is one of the two numbers for the sum
            if (target == 0) continue; //since the program demands two values to be found, should array[i] be the target itself, it must be ignored and loop must continue
            for (int j = i+1; j<sizeof(array)/sizeof(array[0]); j++){ //iterate second value through next element onwards
                if (target >= array[j]){
                    target -= array[j];
                    result[1] = array[j];
                    if (target == 0) goto SUCCESS; //if target is 0 then twoSum has been found
                    target += array[j]; //if target was not reached, undo the removal
                }
                printf("Value2 failed, %d\n", array[j]);
            }
        }
        printf("Value failed, %d\n", array[i]);
        target = sum; //undo the removal if target was not reached with array[i] as first value
    }
    SUCCESS: { //Accepted method of breaking in a nested loop
        printf("Numbers are: %d and %d\n", result[0], result[1]);
        return 0;
    }
    printf("No values have been found\n");
    return 1;
}
