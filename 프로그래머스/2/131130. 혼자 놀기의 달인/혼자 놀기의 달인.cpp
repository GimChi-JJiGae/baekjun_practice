#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> cards) {
    int answer = 0;
    int count1;
    int count2;
    int card_size = cards.size();
    int j;
    int q;
    for(int i = 0; i < card_size; i++){
        vector<int> check(card_size, 0);
        count1 = 0;
        j = cards[i] - 1;
        while(check[j] != 1){
            //cout << j + 1<< endl;
            check[j] = 1;
            count1 += 1;
            j = cards[j] - 1;
        }
        
        for(int k = 0; k < card_size; k++){
            if(check[k] != 1){
                count2 = 0;
                q = cards[k] - 1;
                while(check[q] != 1){
                    check[q] = 1;
                    count2 += 1;
                    q = cards[q] - 1;
                }
                if (count1 * count2 > answer){
                   answer = count1 * count2;
                }
            }
        }
        //cout << "다음" << endl;
        
    }
    
    
    return answer;
}