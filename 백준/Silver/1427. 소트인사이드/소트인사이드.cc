#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool comp(int a, int b){
    return a > b;
}


int main(){
    vector<int> arr;
    string s;
    int tmp;
    cin >> s;
    for(int i = 0; i < s.size(); i++){
        tmp = s[i] - '0';
        arr.emplace_back(tmp);
    }
    
    sort(arr.begin(), arr.end(), comp);
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i];
    }
    
    
    
    
    return 0;
}