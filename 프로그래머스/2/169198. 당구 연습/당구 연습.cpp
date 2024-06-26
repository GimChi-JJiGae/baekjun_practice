#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;
    
    for(int i = 0; i < balls.size(); i++){
        int min_d = 2*(m*m + n*n);
        int case1, case2, case3, case4;
        int x, y;
        x = balls[i][0];
        y = balls[i][1];
        int new_x, new_y;
        // 상 우 하 좌, 시계방향순으로 확인
        
        if(x != startX){
            new_x = x;
            new_y = 2*n - y;
            min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
        } else{
            if(y < startY){
                new_x = x;
                new_y = 2*n - y;
                min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
            }
        }
        
        if(y != startY){
            new_x = 2*m - x;
            new_y = y;
            min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
        } else{
            if(x < startX){
                new_x = 2*m - x;
                new_y = y;
                min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
            }
        }
        
        if(x != startX){
            new_x = x;
            new_y = -y;
            min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
        } else{
            if(y > startY){
                new_x = x;
                new_y = -y;
                min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
            }
        }
        
        if(y != startY){
            new_x = -x;
            new_y = y;
            min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
        } else{
            if(x > startX){
                new_x = -x;
                new_y = y;
                min_d = min(((new_x - startX) * (new_x - startX) + (new_y - startY) * (new_y - startY)), min_d);
                
            }
        }
        
        
        answer.push_back(min_d);
    }
    
    
    return answer;
}