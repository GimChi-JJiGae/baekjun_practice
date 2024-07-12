#include <string>
#include <iostream>

using namespace std;

int main() {
    string s;
    //bool minus = false;
    //bool plus = true;
    int sum_num = 0;
    //int partial_sum = 0;
    cin >> s;
    string tmp;
    bool plus = true;        // 한번 마이너스 되면 다 마이너스 시키면된다.


    for (int i = 0; i < s.size(); i++) {
        char tmp_char = s[i];
        int tmp_int = tmp_char;
        if (tmp_int >= 48 && tmp_int <= 57) {
            tmp.push_back(tmp_char);
        }
        else if (tmp_char == '+') {
            if (plus) {
                sum_num += stoi(tmp);
                tmp = "";
            }
            else {
                sum_num -= stoi(tmp);
                tmp = "";
            }
        }
        else if (tmp_char == '-') {
            if(plus){
                sum_num += stoi(tmp);
                tmp = "";
            }
            else {
                sum_num -= stoi(tmp);
                tmp = "";
            }

            plus = false;
            
        }
    }
    if (plus) {
        sum_num += stoi(tmp);
    }
    else {
        sum_num -= stoi(tmp);
    }

    cout << sum_num;

    return 0;
}