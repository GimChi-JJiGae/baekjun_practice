#include <iostream>
#include <string>
#include <set>

using namespace std;
int main(void){
 
    string arr[1001];
 
    int R,C;
    cin >> R >> C;
    for(int i = 0; i < R; i++){
        cin >> arr[i];
    }
 
    string str[1001];
    for(int i = 0; i < C; i++){
        set<string> s;
        set<string>::iterator iter;
 
        for(int j = 0; j < R; j++){
            str[i] += arr[j][i];
        }
 
        s.insert(str[i]);
    }
 
    for(int i = 0; i < R;i++){
        
    	set<string> s;
    	set<string>::iterator iter;
 
    	for(int j = 0; j < C; j++){
    		if(str[j].size() != 0){
    			str[j].erase(str[j].begin());
 
    			iter = s.find(str[j]);
    			if(iter == s.end()){
    				s.insert(str[j]);
    			}
    			else{
    				if(i == 0){
    					cout << 0;
    					return 0;
    				}
    				cout << i;
    				return 0;
    			}
    		}
 
    	}
    }
    cout << R - 1;
 
}