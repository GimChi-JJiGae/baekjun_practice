#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <cstring>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int n, m, total;
    string s = "", temp = "", k = "";
    
    unordered_set<string>st;

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s;
        st.insert(s);
    }
    
    while (m--) {
        cin >> temp;
        int pos = 0;
        while (pos < temp.length()) {   // . 나누기
            auto it = temp.find(',', pos);  // "" 쓰면 안됨
            if (it == temp.npos) {          // 없을 경우 npos를 반환하기 때문
                k = temp.substr(pos);
                if (st.find(k) != st.end()) {   // 찾는데 없으면 .end()를 반환하기 때문
                    st.erase(k);
                }
                break;  // 한 단어 였으니 탈출
            }
            else {
                k = temp.substr(pos, it - pos);
                if (st.find(k) != st.end()) {
                    st.erase(k);
                }
                pos = it + 1;

            }
            
        }
        cout << st.size() << "\n";
    }
    return 0;
}
