#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    int s = 0, e = 0;
    int sum = sequence[0];
    int subLen = sequence.size() + 1;
    pair<int, int> result;
    
    while (s <= e && e < sequence.size()) {
        if (sum < k){               // 더 넣어야함
            e += 1;
            sum += sequence[e];  
        } 
        else if (sum == k) {        // 같음
            if (e-s+1 < subLen) {   // 길이가 더 짧은 수열이면
                subLen = e-s+1;
                result = {s, e};
            } else if (e-s+1 == subLen) {
                if (s < result.first) { // 시작 인덱스가 더 작으면
                    result = {s, e};
                }
            }
            
            sum -= sequence[s];     // 다음단계로 넘어가자
            s += 1;
        } 
        else {                      // 크니까 앞에서 빼줌
            sum -= sequence[s];
            s += 1;
        }
    }
    
    return {result.first, result.second};
}