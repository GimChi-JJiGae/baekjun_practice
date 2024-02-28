#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;
// x^2 + y^2 = r^2

long long calrange(int y, int r, int ty){
    long long result;
    double tmp = sqrt(pow(r, 2) - pow(y, 2));
    if(ty == 2){
        double tmp_floor = floor(tmp);
        result = round(tmp_floor);
    }
    else{
        double tmp_ceil = ceil(tmp);
        result = round(tmp_ceil); // 형변환시 2.0이 자꾸 1이돼서 반올림으로 바꿈
        
    }
    
    return result;
}
long long solution(int r1, int r2) {
    long long answer = 0;
    long long cnt = 0;
    for(int i = r2; i > 0; i--){
        long long point_range = calrange(i, r2, 2);

        
        if(i >= r1 ){
            cnt += point_range * 2 + 1;
        } else{
            long long limit_range = calrange(i, r1, 1);
        
            cnt += (point_range - limit_range + 1) * 2;
        }
    }

    cnt = cnt * 2;
    cnt += (r2 - r1 + 1) * 2;
    
    answer = cnt;
    
    return answer;
}