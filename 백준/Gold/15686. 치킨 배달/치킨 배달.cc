#include <iostream>
#include <vector>


using namespace std;

int homeToChicken[101][27]; // 다른 함수에서 사용하기 위해 전역변수로 설정
int minChicken = 10000;     // 최소 치킨거리
int homeIdx = 0;
int chickenIdx = 0;

//조합 함수
void generateCombinations(vector<int>& combination, int start, int n, int m) {
    // 조합이 완성된 경우 결과를 출력
    if (combination.size() == m) {
        int tmp = 0;

        for (int k = 0; k < homeIdx; k++) {
            int bestTmp = 150;
            for (int num : combination) {
                
                bestTmp = min(bestTmp, homeToChicken[k][num]);      // 살아남은 치킨집 중 가장 가까운곳 찾기
            }
            tmp += bestTmp;
        }
        /*for (int num : combination) {
            cout << num << " ";
            for (int k = 0; k < homeIdx - 1; k++) {
                tmp += homeToChicken[k][num];
            }
        }*/
        /*cout << endl;
        cout << tmp << endl;*/
        if (tmp < minChicken) {
            minChicken = tmp;
        }
        return;
    }

    // 조합 생성
    for (int i = start; i <= n; ++i) {
        combination.push_back(i);
        generateCombinations(combination, i + 1, n, m);
        combination.pop_back();
    }
}


int main()
{
    int N, M;
    int city[51][51];
    pair<int, int> home[101];
    pair<int, int> chicken[27];
    
    int p = 0;

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int tmp;
            p++;
            cin >> tmp;
            city[i][j] = tmp;
            if (tmp == 1) {
                home[homeIdx].first = i;
                home[homeIdx].second = j;
                homeIdx++;
            }
            if (tmp == 2) {
                chicken[chickenIdx].first = i;
                chicken[chickenIdx].second = j;
                chickenIdx++;
            }
        }
    }

    // 각 집별 각 치킨집까지의 거리를 저장
    for (int i = 0; i < homeIdx; i++) {
        for (int j = 0; j < chickenIdx; j++) {
            homeToChicken[i][j] = abs(home[i].first - chicken[j].first) + abs(home[i].second - chicken[j].second);

        }
    }

    vector<int> combination;
    generateCombinations(combination, 0, chickenIdx - 1, M);

    cout << minChicken;

    return 0;
}