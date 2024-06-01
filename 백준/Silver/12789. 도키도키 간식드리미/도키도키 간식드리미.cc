#include <stack>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int N;
    int now = 1;
    bool check = false;
//    scanf("%d", &N);
//    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    stack<int> st;
    string n_string;
    string input;

    getline(cin, n_string);

    N = stoi(n_string);
    getline(cin, input);

    istringstream iss(input);
    int num;
    vector<int> nums;

    while (iss >> num) {
        nums.push_back(num);
    }

    for (const auto& num : nums) {
        if (now == num) {
            now++;
            while (!st.empty() and st.top() == now) {
                st.pop();
                now++;
            }
            continue;
        }
        else {
            if (!st.empty() and st.top() < num) {
                check = true;
                break;
            }
            else {
                st.push(num);
            }
        }
    }

    if (check) {
        cout << "Sad";
    }
    else {
        if (st.empty()) {
            cout << "Nice";
        }
        else {
            cout << "Sad";
        }
    }
    return 0;
}