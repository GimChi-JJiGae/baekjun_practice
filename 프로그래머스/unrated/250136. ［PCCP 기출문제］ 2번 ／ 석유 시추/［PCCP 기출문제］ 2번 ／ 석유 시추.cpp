#include <string>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int BFS(vector<vector<int>>& data, vector<vector<int>>& origin, int n, int m, int c_i, int c_j, int numbering){
    
    int oil_count = 1;
    queue<pair<int, int>> bfsQueue;
    
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};
    
    bfsQueue.push({c_i, c_j});
    origin[c_i][c_j] = numbering;
    
    while (!bfsQueue.empty()) {
        pair<int, int> current = bfsQueue.front();
        bfsQueue.pop();

        int currentRow = current.first;
        int currentCol = current.second;
        
        // origin[currentRow][currentCol] = numbering;
        
        for (int i = 0; i < 4; ++i) {
            int newRow = currentRow + dr[i];
            int newCol = currentCol + dc[i];

            // 범위 체크 및 방문 여부 확인
            if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && origin[newRow][newCol] == 0 && data[newRow][newCol] == 1) {
                bfsQueue.push({newRow, newCol});
                origin[newRow][newCol] = numbering;
                oil_count++;
                
            }
        }
    }
    
    return oil_count;
}

int solution(vector<vector<int>> land) {
    int answer = 0;
    int n = land.size();
    int m = land[0].size();
    int number = 1;

    vector<vector<int>> visited(n, vector<int>(m, 0));
    vector<int> oil_info(n*m, 0); // 몇번쨰 number의 오일의 크기 파악
    // BFS(visited, n, m, 0, 0, number);
    // number++;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(land[i][j] == 1 && visited[i][j] ==0){
                int tmp = BFS(land, visited, n, m, i, j, number);
                oil_info[number] = tmp;
                number++;
            }
        }
    }
    
    for(int b = 0; b < m; b++){
        set<int> uniqueSet;
        vector<int> valueSum;
        int before = 0;
        for(int a = 0; a < n; a++){
            if(visited[a][b] != before && visited[a][b] != 0 && uniqueSet.find(visited[a][b]) == uniqueSet.end()){
                valueSum.push_back(visited[a][b]);
                uniqueSet.insert(visited[a][b]);
                before = visited[a][b];
            }
        }
        int tmp_sum = 0;
        for(int t = 0; t < valueSum.size(); t++){
            tmp_sum += oil_info[valueSum[t]];
        }
        if (tmp_sum > answer){
            answer = tmp_sum;
        }
    }
    
    return answer;
    
    
}