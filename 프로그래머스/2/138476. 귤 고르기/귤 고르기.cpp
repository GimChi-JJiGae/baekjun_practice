#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

static bool comp(pair<int, int>& a, pair<int, int>& b){
    return a.second > b.second;
}


int solution(int k, vector<int> tangerine) {
    int answer = 0;
    int length = tangerine.size();
    
    map<int, int> fruits;
    
    for(int i = 0; i < length; i++){
        auto it = fruits.find(tangerine[i]);
        if (it != fruits.end()){
            fruits[tangerine[i]] += 1;
        }else{
            fruits[tangerine[i]] = 1;
        }
    }
    
    
    // 위에서 일단 데이터를 집어넣은 후 아래에서 정렬
    vector<pair<int, int>> v(fruits.begin(), fruits.end());
    
    sort(v.begin(), v.end(), comp);
    
    int left = k;
    int idx = 0;
    int max_size = v.size();
    
    while(left > 0){
        if(v[idx].second <= left){
            left -= v[idx].second;
            idx += 1;
            
            answer++;
            
            if(idx >= max_size){
                break;
            }
        }else{
            answer++;
            left = 0;
        }
        
    }
    
    return answer;
}