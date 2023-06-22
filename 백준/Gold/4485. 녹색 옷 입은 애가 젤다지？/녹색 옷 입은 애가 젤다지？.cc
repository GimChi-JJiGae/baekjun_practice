#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int y_ar[4] = { 0,0,-1,1 };
int x_ar[4] = { 1,-1,0,0 };
int n;
int arr[130][130];
int dist[130][130];

void bfs() {

	queue <pair<int, int>> pq;

	pq.push(make_pair(0, 0));
	dist[0][0] = arr[0][0];
    
	while (!pq.empty()) {
		
		int y = pq.front().first;
		int x = pq.front().second;
		pq.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + y_ar[i];
			int nx = x + x_ar[i];
			

			if (ny >= 0 && ny < n && nx >= 0 && nx < n) {
				if ( dist[ny][nx] > dist[y][x] + arr[ny][nx]) {
					dist[ny][nx] = dist[y][x] + arr[ny][nx];
					pq.push(make_pair(ny, nx));
				}
			}
		}
	}

}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	int cnt = 1;

	while (1) {
		cin >> n;
		if (n == 0)
			break;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				cin >> arr[i][j];
				dist[i][j] = 2000000000;
			}
		
		bfs();
		cout << "Problem " << cnt++ << ": " << dist[n - 1][n - 1] << "\n";
	}

	return 0;
}