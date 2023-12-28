#include <iostream>
#include <string>
using namespace std;
int solution(string s)
{
    int answer=1;
    

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for(int i = 0; i < s.size(); i++){
        
        if(i < s.size() - 1){
            if(s[i] == s[i + 1]){
                int till;
                if( i > s.size() - i - 2){
                    till = s.size() - i - 2;
                }else{
                    till = i;
                }
                
                int cnt = 2;
                for (int j = 1; j <= till; j++){
                    if (s[i - j] == s[i + 1 + j]){
                        cnt +=2;
                    } else{
                        break;
                    }
                }
                if(cnt > answer){
                    answer = cnt;
                }
                
                //continue;
            }
        }
        
        
        
        int till;// = max(i, s.size() - i - 1);
        
        if( i > s.size() - i - 1){
            till = s.size() - i - 1;
        } else{
            till = i;
        }
        //cout << "틸확인" << till << endl;
        
        
        int cnt = 1;
        for (int j = 1; j <= till; j++){
            if(s[i - j] == s[i + j]){
                cnt += 2;
            }
            else{
                break;
            }
        }
        // cout << cnt << endl;
        if(answer < cnt){
            answer = cnt;
        }
    }

    return answer;
}