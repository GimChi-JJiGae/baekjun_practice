#include <iostream>
#include <string>

using namespace std;

int main(){
    
    string str;
    char tmp;
    int tmp_num, s;
    s = 0;
    cin >> str;
    for(int i = 0; i < str.size(); i++){
        tmp = str[i];
        if(tmp == ' '){
            s += 2;
        } else {
            tmp_num = (int)tmp - 65;
            if(tmp_num < 0){
                s += 11;
            } else {
                if(tmp_num == 15 || tmp_num == 16 || tmp_num == 17 || tmp_num == 18){
                    s += 8;
                } else if(tmp_num == 19 || tmp_num == 20 || tmp_num == 21){
                    s += 9;
                } else if(tmp_num == 22 || tmp_num == 23 || tmp_num == 24 || tmp_num == 25){
                    s += 10;
                } else {
                    s += (tmp_num / 3) + 3;    
                }
                
            }
        }  
    }
    cout << s;    
    
    
    return 0;
}