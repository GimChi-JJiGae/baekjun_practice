#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> targets)
{
    int answer = 0, idx = 0;
    sort(targets.begin(), targets.end());
    while (idx < targets.size())        //요격을 다할때까지
    {
        int end = targets[idx++][1];    // 타겟의 e 설정
        answer++;
        while (idx < targets.size() && targets[idx][0] < end)
        {
            
            if (targets[idx][1] < end){
                end = targets[idx][1];
            }
            idx++;
        }
    }
    return answer;
}