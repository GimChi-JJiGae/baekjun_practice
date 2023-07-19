
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string abList;
    int aNum = 0;
    int bNum = 0;

    cin >> abList;

    for (int i = 0; i < abList.size(); i++) {
        if (abList[i] == 'a') {
            aNum++;
        }
        else {
            bNum++;
        }
    }
    if (bNum == 0 || aNum == 0 || bNum == 1 || aNum == 1) {
        cout << 0;
        return 0;
    }

    int minB = bNum;

    for (int i = 0; i < abList.size(); i++) {
        int tmp = 0;
        for (int j = 0; j < aNum; j++) {
            if (i + j < abList.size()) {        // 문자열 길이보다 짧음
                if (abList[i + j] == 'b') {
                    tmp++;
                }
            }
            else {                          // 문자열길이 넘어가는 경우
                if (abList[i + j - abList.size()] == 'b') {
                    tmp++;
                }
            }
        }
        if (tmp < minB) {
            minB = tmp;
        }
    }
    cout << minB;
    return 0;
}
