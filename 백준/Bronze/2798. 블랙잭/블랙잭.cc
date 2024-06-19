#include <iostream>
#include <vector>


using namespace std;

int main(){
    
    int n, m;
    int max_val = 0;
    cin >> n >> m;
    vector<int> cards(n);
    int tmp;
    for(int i = 0; i < n; i++){
        cin >> tmp;
        cards[i] = tmp;
    }
    int tmp_val;
    for(int i = 0; i < n - 2; i++){
        for(int j = i + 1; j < n - 1; j++){
            for(int k = j + 1; k < n; k++){
                tmp_val = cards[i] + cards[j] + cards[k];
                if(tmp_val > max_val && tmp_val <= m){
                    max_val = tmp_val;
                }
            }
        }
    }
    
    cout << max_val;
    
    
    return 0;
}