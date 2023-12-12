#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> scores) {
    int wanho = scores[0][0] + scores[0][1];
    int answer = 0;
    vector<int> bigger_list;

    
    for (int i = 0; i < scores.size(); i++) {
        if (scores[i][0] + scores[i][1] > wanho) {
            bigger_list.push_back(i);
        }
    }
    int pre_cnt = bigger_list.size();
    // for (int q = 0; q < pre_cnt; q++){
    //     cout << bigger_list[q] << " ";
    // }

    for (int j = 0; j < bigger_list.size(); j++){
        if (scores[bigger_list[j]][0] > scores[0][0] and scores[bigger_list[j]][1] > scores[0][1]) {
            return -1;
        }
        else {
            for (int k = 0; k < bigger_list.size(); k++) {
                if (scores[bigger_list[k]][0] > scores[bigger_list[j]][0] and scores[bigger_list[k]][1] > scores[bigger_list[j]][1]) {    // 인센티브 대상이 아니면
                    pre_cnt--;
                    // cout << scores[bigger_list[k]][0] << " " << scores[bigger_list[k]][1] << endl;
                    // cout << "위가 더 큼";
                    // cout << scores[j][0] << " " << scores[j][1] << endl;
                    
                    break;
                }
            }
        }
    }
    answer = pre_cnt + 1; // 자기자신 등수니까 + 1
    return answer;
}
