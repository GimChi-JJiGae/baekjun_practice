#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

map<int, vector<int>> mapping;
set<int> heads;
set<int> tails;
map<int, bool> visited;

int check_type(int start, int now){
    if(mapping.find(now) == mapping.end()){     // 막대, 막대는 돌아오지 못함
        return 2;
    }
    if(mapping[now].size() == 2){               // 8자, 8자는 원래자리로 오기전 갈림길을 만남
        return 3;
    }
    if(mapping[now][0] == start){               // 도넛, 도넛은 갈림길없이 돌아옴
        return 1;
    }
    return check_type(start, mapping[now][0]);
}

vector<int> solution(vector<vector<int>> edges) {
    vector<int> answer;
    vector<int> suspects;       // 추가된 것으로 의심되는 노드, 막대 그래프 중간에 꽂히면 용의자가 여럿임
    int added;      // 추가된 노드
    int count;      // 그래프 수
    for(int i = 0; i < edges.size(); i++){
        
        // 연결 정리
        heads.insert(edges[i][0]);
        tails.insert(edges[i][1]);
        
        if(mapping.find(edges[i][0]) != mapping.end()){
            mapping[edges[i][0]].push_back(edges[i][1]);
        }else{
            mapping[edges[i][0]] = vector<int>{edges[i][1]};
        }
        
        
    }
    
    set_difference(heads.begin(), heads.end(), tails.begin(), tails.end(), back_inserter(suspects));
    
    for(int i = 0; i < suspects.size(); i++){
        if(mapping[suspects[i]].size() > 1){        // 추가된것은 꼬리를 그래프 수만큼 달고 있으므로
            count = mapping[suspects[i]].size();
            added = suspects[i];
            break;
        }
    }
    answer.push_back(added);
    
    int tmp1 = 0;
    int tmp2 = 0;
    int tmp3 = 0;           // 하나씩 안넣어줘서 오류 발생..
    for(int i = 0; i < count; i++){
        int start = mapping[added][i];
        int tmp = check_type(start, start);
        //cout << tmp << endl;
        if(tmp == 1) {
            tmp1++;
        } else if(tmp == 2){
            tmp2++;  
        } 
        else {
            tmp3++;
        }
    }
    answer.push_back(tmp1);
    answer.push_back(tmp2);
    answer.push_back(tmp3);
    return answer;
}