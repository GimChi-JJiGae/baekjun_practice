#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

typedef pair<int, int> pii;

const int INF = INT_MAX;

int main() {
    int N, tc = 1;
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
    
    while (true) {
        cin >> N;
        
        if (N == 0) {
            break;
        }
        
        vector<vector<int>> cave(N, vector<int>(N));
        vector<vector<int>> dist(N, vector<int>(N, INF));
        vector<vector<int>> cost(N, vector<int>(N));
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> cave[i][j];
            }
        }
        
        dist[0][0] = cave[0][0];
        
        priority_queue<pair<int, pii>, vector<pair<int, pii>>, greater<pair<int, pii>>> pq;
        pq.push({ cave[0][0], {0, 0} });
        
        while (!pq.empty()) {
            int x = pq.top().second.first;
            int y = pq.top().second.second;
            int d = pq.top().first;
            pq.pop();
            
            if (d > dist[x][y]) {
                continue;
            }
            
            int dx[4] = {-1, 1, 0, 0};
            int dy[4] = {0, 0, -1, 1};
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    int nd = d + cave[nx][ny];
                    
                    if (nd < dist[nx][ny]) {
                        dist[nx][ny] = nd;
                        pq.push({ nd, {nx, ny} });
                    }
                }
            }
        }
        
        cout << "Problem " << tc << ": " << dist[N - 1][N - 1] << endl;
        tc++;
    }
    
    return 0;
}