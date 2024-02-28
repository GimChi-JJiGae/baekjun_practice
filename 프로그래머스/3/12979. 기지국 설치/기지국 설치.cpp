#include <iostream>
#include <vector>
using namespace std;

int solution(int n, vector<int> stations, int w)
{
    int answer = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    int now = 1;
    int target;
    int toFill;
    for(int i = 0; i < stations.size(); i++){   // 설치된 기지국의 왼쪽만 뽑아보자
        
        target = stations[i] - w;
        if(target <= now){      // 왼쪽 다 채운 경우
            now = stations[i] + w + 1;
            continue;
        }
        else{
            toFill = target - now;  // 채워야하는 칸수
            answer += toFill / (w*2 + 1);
            if(toFill % (w*2 + 1) != 0){
                answer += 1;            // 깔끔하게 다 못채워서 추가로 채움
            }
            now = stations[i] + w + 1;
        }
    }
    if(now > n){
        return answer;
    } else{
        toFill = n - now + 1;
        answer += toFill / (w*2 + 1);
        if(toFill % (w*2 + 1) != 0){
            answer += 1;
        }
    }
    
    return answer;
}