#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    
    
    int m, r;
    
    if(s < n){
        vector<int> tmp(1, -1);
        return tmp;
    }
    
    m = s / n;
    r = s % n;
    
    vector<int> answer(n, m);
    for(int i = n - 1; i > n - 1 - r; i--){
        answer[i] = answer[i] + 1;
    }
    
    return answer;
}