#include <string>
#include <vector>

using namespace std;


string hexToDec(long long num) {            // 이진법으로 변경
    string ret = "";
    while (num) {
        ret = to_string(num % 2) + ret;
        num /= 2;
    }
    return ret;
}

string changeToFullDec(string str) {        // 포화 이진트리에 맞게 변경
    string ret = str;
    int idx = 2;
    while (true) {
        if (str.length() <= idx - 1) {
            break;
        }
        idx *= 2;
    }
    for (int i = 0; i < idx - 1 - str.length(); i++) ret = "0" + ret;
    return ret;
}

bool isAllZero(string str) {            // 만약 모두 0인 경우
    for (char c : str) {
        if (c != '0') return false;
    }
    return true;
}

bool canDraw(string str) {                  // 분할하여 확인
    if (str.length() == 1 ) return true;
    if (isAllZero(str)) return true;
 
    int midIdx = str.length() / 2;
    string left = str.substr(0, midIdx);
    string right = str.substr(midIdx + 1);
 
    if (str[midIdx] == '1' && canDraw(left) && canDraw(right)) return true;
    else return false;
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    
    for(int i = 0; i < numbers.size(); i++){
        string dec = hexToDec(numbers[i]);
        string fullDec = changeToFullDec(dec);
        if (canDraw(fullDec)){
            answer.push_back(1);
        }
        else{
            answer.push_back(0);
        }
    }
    
    return answer;
}

