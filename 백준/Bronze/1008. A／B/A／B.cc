#include <stdio.h>
 
int main(int argc, char const *argv[]) {
    double a;
    double b;
 
    scanf("%lf %lf", &a, &b);	// double 입력은 %lf 

    printf("%.13lf", a / b);	// 유효숫자가 13개 
    
    return 0;
}