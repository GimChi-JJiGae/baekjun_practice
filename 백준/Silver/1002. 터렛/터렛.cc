#include <iostream>
#include <cmath>

using namespace std;

int main(){
    
    double T, x1, y1, r1, x2, y2, r2;
    double distance;
    double sub;
    cin >> T;
    for (int i = 0; i < T; i++){
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        distance = sqrt(pow((x1 - x2),2) + pow((y1 - y2),2));
    
        sub = r1 > r2 ? r1 - r2 : r2 - r1;
        
        if(distance == 0 && r1 != r2){
            cout << 0;
        } else if (distance == 0 && r1 == r2){
            cout << -1;
        } else if (r1 + r2 == distance || sub == distance){
            cout << 1;
        } else if (sub < distance && distance < (r1 + r2)){
            cout << 2;
        } else {
            cout << 0;
        }
        cout << "\n";
    }

    return 0;
}

