#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

stack<int> st;
int x, y, arr[501];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> x >> y;
	for (int i = 0; i < y; i++) {
		cin >> arr[i];
	}
	int answer = 0;

	for (int i = 1; i < y; i++) {
		int left = *max_element(arr, arr + i);
		int right = *max_element(arr + i + 1, arr + y);
		int cur = arr[i];
		if (cur < left && cur < right) {
			answer += min(left, right) - cur;
		}
	}
	cout << answer;
}