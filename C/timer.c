//Timer ported from python
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#define LIMIT 360000 //100h is the limit of all input
#define FALSE 0
#define TRUE 1

/*
note for the future: try and make functions that can be tested for accuracy
*/
enum {INSTRUCT, NAN, }

typedef struct time {
    int xx, yy, zz;
} time;

void errorhandler(int input){ //handles all possible cases of input error
    if (input == INSTRUCT){ //Misinput on command line
        printf("To use: /timer countup\n        /timer countdown time [m for minutes] \n");
        exit(0);
    }
    if (input == NAN) {} //countdown input is not a 
        fprintf(stderr, "Input is not a positive number.\n");
        exit(0);
    }
}

void incrementer(time *t){ //handles overflow of time
    ++t->xx;
    if (t->xx == 60) {
        ++t->yy;
        t->xx = 0;
    }
    if (t->yy == 60){
        ++t->zz;
        t->yy = 0;
    }
}

void decrementer(time *t){ //handles overflow of time but for negatives
    --t->xx;
    if (t->xx == -1){
        --t->yy;
        t->xx = 59;
    }
    if (t->yy == -1){
        --t->zz;
        t->yy = 59;
    }
}
void countup(){ //countup function
    int secs = 0;
    time timeData = {0, 0, 0};
    time *t = &timeData;
    while (1){
        sleep(1);
        ++secs;
        incrementer(t);
        if (secs == LIMIT) break;
        printf("%02d:%02d:%02d %ds\n", t->zz, t->yy, t->xx, secs);
    }
    printf("Maximum time reached!\n");
}

void countdown(int t, int minute){
    int secs = 0;
    time timeData = {0,0,0};
    time *tp = &timeData;
    switch (minute) { //switch statement handling the construction of hours, mins, secs, and the secs variable
        case TRUE: {
            secs = t*60;
            tp->xx = secs/60; tp->yy = t%60; tp->zz = t/60;
            break;
        }
        default: {
            secs = t;
            tp->xx = secs/60; tp->yy = t/60; tp->zz = t/3600;
            break;
        }
    }
    while (1){
        sleep(1);
        --secs;
        decrementer(tp);
        if (secs == -1) break;
        printf("%02d:%02d:%02d %ds\n", tp->zz, tp->yy, tp->xx, secs);
    }
    printf("Finished!\n");
}

int main(int n, char *args[n]){
    setbuf(stdout, NULL);
    if (n == 1){ //maybe a test module
        errorhandler(INSTRUCT);
        return 0;
    }
    if (n == 2 && strcmp("countup", args[1]) == 0){
        countup();
        return 1;
    }
    // https://youtu.be/M2dhD9zR6hk
    else if (strcmp("countdown", args[1]) == 0 && (n == 2 || n == 3)){
        for (int count = 0; count < strlen(args[2]); ++count){ //checks that args[2] is a number
            switch (isdigit(args[2][count])){
                case 0: {//NaN
                errorhandler(NAN)
                } 
                default: {
                    break;
                }
            }
        }
        int time = atoi(args[2]);
        int min;
        if (time >= LIMIT) {fprintf(stderr, "Input is at or above the limit of 100h.\n"); exit(0);}
        if (n == 3) {//if the m was included, grabs it, checks if it is indeed an m, then says that minutes is true for the funct
            if (strcmp("m", args[3])!=0) {fprintf(stderr, "Last argument is not an \"m\".\n"); exit(0);}
            else {min = TRUE;}
        }
        else {min = FALSE;}
        countdown(time, min);
        return 1;
    }
    else {
        errorhandler(INSTRUCT);
    }
    return 0;
}
