
#include <iostream>
#include <algorithm>

using namespace std;

int cost[8][8];
int dp[8][8][3]; 
int N, M;

int solve(int x, int y, int dir)
{
    if (x == N) // 범위 밖
    {
        return 0;
    }

    if (dp[x][y][dir] != 4000)              // 6 * 6 * 100 을 넘을수없음
    {
        return dp[x][y][dir];
    }

    // 왼쪽
    if (dir != 0 && y - 1 >= 0)         // 이전이 왼쪽이 아니면
    {
        dp[x][y][dir] = solve(x + 1, y - 1, 0) + cost[x][y];
    }

    // 중앙 
    if (dir != 1)                       // 이전이 중앙이 아니면
    {
        dp[x][y][dir] = min(dp[x][y][dir], solve(x + 1, y, 1) + cost[x][y]);
    }

    // 오른쪽
    if (dir != 2 && y + 1 < M)          // 이전이 오른쪽이 아니면
    {
        dp[x][y][dir] = min(dp[x][y][dir], solve(x + 1, y + 1, 2) + cost[x][y]);
    }

    return dp[x][y][dir];
}

int main(void)
{

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> cost[i][j];

            for (int k = 0; k < 4; k++)
            {
                dp[i][j][k] = 4000;
            }
        }
    }

    int Min = 4000;
    for (int i = 0; i < M; i++)
    {
        // 처음에는 방향이 없기 때문에 dir에 3을 대입 
        Min = min(Min, solve(0, i, 3));
    }

    cout << Min;

    return 0;
}