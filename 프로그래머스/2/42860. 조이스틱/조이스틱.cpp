#include <string>
#include <vector>

using namespace std;

int alpha[26] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

int solution(string name) {
    int answer = 0;
    
    int n = name.length();
    
    int min_move = n - 1;   // 한 방향으로 가는 경우
    
    for(int i = 0; i < n; i++){
        answer += alpha[name[i] - 'A'];
        
        int j  = i + 1;
        while(j < n and name[j] == 'A'){
            j++;
        }
        min_move = min(min_move, i + n - j + min(i, n - j));
    }
    
    answer += min_move;
    
    
    return answer;
}