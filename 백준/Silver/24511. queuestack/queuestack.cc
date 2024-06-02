#include <iostream>
#include <vector>
#include <sstream>
#include <queue>
#include <stack>

using namespace std;

int main() {
    queue<int> bigQ;
    int N, M;
    string temp;
    int temp_number;
    vector<int> elements;
    vector<int> setting;


    getline(cin, temp);
    istringstream iss1(temp);
    iss1 >> N;
    getline(cin, temp);
    istringstream iss2(temp);
    while (iss2 >> temp_number) {
        setting.push_back(temp_number);
    }
    getline(cin, temp);
    int idx = 0;
    istringstream iss3(temp);
    while (iss3 >> temp_number) {
        elements.push_back(temp_number);
        if (setting[idx] == 0) {
            bigQ.push(temp_number);
        }
        idx++;
    }


    stack<int> stack_to_reverse;
    queue<int> reversed_bigQ;
    int size = bigQ.size();
    for (int i = 0; i < size; i++) {
        stack_to_reverse.push(bigQ.front());
        bigQ.pop();
    }
    for (int j = 0; j < size; j++) {
        reversed_bigQ.push(stack_to_reverse.top());
        stack_to_reverse.pop();
    }


    getline(cin, temp);
    istringstream iss4(temp);
    iss4 >> M;

    getline(cin, temp);
    istringstream iss5(temp);
    int result;
    while (iss5 >> temp_number) {
        reversed_bigQ.push(temp_number);
        result = reversed_bigQ.front();
        reversed_bigQ.pop();
        cout << result << " ";
    }
    return 0;

}