#include <iostream>

int main(){
    int T, a, b, tmp = 1;
    scanf("%d",&T);
    for(int i=0; i<T; i++){
        scanf("%d %d",&a,&b);
        for(int j=0; j<b; j++){
            tmp = (tmp * a) % 10;
        }
        if(tmp == 0){
            printf("10\n");
        } else {
            printf("%d\n",tmp);
        }
        tmp = 1;
    }

    return 0;
}