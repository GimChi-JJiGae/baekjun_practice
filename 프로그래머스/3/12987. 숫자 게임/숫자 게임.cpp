#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = -1;
    
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    
    int cnt = 0;
    int a_idx = 0;
    for(int i = 0; i < B.size(); i++){
        if(A[a_idx] < B[i]){
            cnt += 1;
            a_idx += 1;
        }
        else if(A[a_idx] < B[i]){
            a_idx += 1;
        }
    }
    answer = cnt;
    return answer;
}


