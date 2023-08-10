#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int dp[101];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    vector<pair<int, int>> vt;
    cin >> n;
    vt.push_back({ 0,0 });
    for (int i = 1; i <= n;i++) {
        int a, b;
        cin >> a >> b;
        vt.push_back({ a,b });

    }
    sort(vt.begin(),vt.end());
    dp[1] = 1;
    int ans = 100;

    for (int i = 2; i <= n; i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (vt[i].second > vt[j].second) {
                if(dp[i]<=dp[j])
                dp[i] = dp[j] + 1;
            }
        }
    }
    for(int i=1; i<=n;i++)
    ans = min( ans,n - dp[i]);
    cout << ans;
    return 0;
}