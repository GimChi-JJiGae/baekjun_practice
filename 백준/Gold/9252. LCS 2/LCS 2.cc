#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	
	string str1, str2;
	string result = "";
	int max_length = 0;
	cin >> str1;
	cin >> str2;


	int size1 = str1.size();
	int size2 = str2.size();

	vector<vector<int>> matrix(size1 + 1, vector<int>(size2 + 1, 0));
	for (int i = 0; i < size1; i++) {
		for (int j = 0; j < size2; j++) {
			if (str1[i] == str2[j]) {
				matrix[i + 1][j + 1] = matrix[i][j] + 1;
			}
			else {
				matrix[i + 1][j + 1] = max(matrix[i][j + 1], matrix[i + 1][j]);
			}
		}
	}

	vector<char> reversed_result;

	int value = matrix[size1][size2];
	int now_i = size1;
	int now_j = size2;
	cout << value << endl;
	while (value > 0) {
		if (matrix[now_i][now_j] == matrix[now_i - 1][now_j]) {
			now_i -= 1;
		}
		else if(matrix[now_i][now_j] == matrix[now_i][now_j - 1]) {
			now_j -= 1;
		}
		else {
			now_i -= 1;
			now_j -= 1;
			value = matrix[now_i][now_j];
			reversed_result.push_back(str1[now_i]);
		}
	}
	for (int i = reversed_result.size() - 1; i >= 0; i--) {
		cout << reversed_result[i];
	}




	return 0;
}