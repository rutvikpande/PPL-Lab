#include<stdio.h>
void function() {
        char buffer1[5];
        
        char *ret;
        ret =buffer1 + 21*sizeof(char);
        (*ret) += 7;
}

void main() {
        int x;
        x = 0;
        function(1,2,3);
        x = 1;
        printf("%d\n",x);
}
