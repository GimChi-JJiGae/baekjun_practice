#include<iostream>

using namespace std;

int N, minX, maxX, minY, maxY, tmpA, tmpB;
int width, height;

int main(){
    minX = 100000;
    minY = 100000;
    maxX = -100000;
    maxY = -100000;
    cin >> N;
    if (N == 1){
        cout << 0;
        return 0;
    }
    for(int i = 0; i < N; i++){
        cin >> tmpA >> tmpB;
        if (minX > tmpA){
            minX = tmpA;
        }
        if (minY > tmpB){
            minY = tmpB;
        }
        if (maxX < tmpA){
            maxX = tmpA;
        }
        if (maxY < tmpB){
            maxY = tmpB;
        }
    }
    
    width = maxX -minX;
    height = maxY - minY;
    
    cout << width * height;
  
    return 0;
}