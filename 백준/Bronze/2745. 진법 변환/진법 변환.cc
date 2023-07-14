
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    string num;
    int rule;
    
    cin >> num;
    cin >> rule;

    int total = 0;

    if (rule > 10) {
        for (int i = 0; i < num.size(); i++) {
            char tmp = num[i];
            if ((int)tmp > 64) {
                int to_ten = (int(tmp) - 55) * pow(rule, num.size() - i - 1);
                total += to_ten;
            }
            else {
                int to_ten = (int(tmp) - 48) * pow(rule, num.size() - i - 1);
                total += to_ten;
            }
            
        }
    }
    else {
        for (int i = 0; i < num.size(); i++) {
            int tmp = num[i] - '0';
            int to_ten = tmp * pow(rule, num.size() - i - 1);
            total += to_ten;
        }
    }

    cout << total;
    
}