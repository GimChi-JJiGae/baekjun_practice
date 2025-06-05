#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    unordered_set<string> users;
    int hi = 0;

    string user;
    
    for (int i = 0; i < N; i++) {
        cin >> user;
        if (user == "ENTER") {
            hi += users.size();
            users.clear();
         
            continue;
        }
        users.insert(user);
    }
    hi += users.size();
    cout << hi;
    return 0;
}