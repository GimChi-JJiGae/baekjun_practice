// #include <string>
// #include <vector>

// using namespace std;

// //F(n) = 3*F(n-2) + 2F(n-4) + 2F(n-6)

// int cal(int n, vector<int>& dt) {
//     if (n == 2) {
//         return dt[2];
//     } else if (n == 4) {
//         return dt[4];
//     } else if (n == 6) {
//         return dt[6];
//     } else {
//         int tmp1, tmp2, tmp3;
//         if(dt[n-2] != 0){
//             tmp1 = dt[n-2];
//         } else{
//             tmp1 = cal(n-2, dt);
//         }
        
//         if(dt[n-4] != 0){
//             tmp2 = dt[n-4];
//         } else{
//             tmp2 = cal(n-4, dt);
//         }
        
//         if(dt[n-6] != 0){
//             tmp3 = dt[n-6];
//         } else{
//             tmp3 = cal(n-6, dt);
//         }
        
//         return 3*tmp1 + 2*tmp2 + 2*tmp3;
        
        
// //         if (dt[n - 2] != 0 and dt[n - 4] != 0 and !dt[n - 6]) {
// //             dt[n] = 3 * dt[n - 2] + 2 * dt[n - 4] + 2 * dt[n - 6];
// //             return dt[n];
// //         } else {
            
// //             dt[n] = 3 * cal(n - 2, dt) + 2 * cal(n - 4, dt) + 2 * cal(n - 6, dt); 
// //             return dt[n];
// //         }
//     }
// }

// int solution(int n) {
//     vector<int> dt(5001, 0);
//     dt[2] = 3;
//     dt[4] = 11;
//     dt[6] = 41;
//     int answer = cal(n, dt);
//     return answer;
// }

#include <string>
#include <vector>
#define MOD 1000000007

using namespace std;

long long arr[5001];


int solution(int n) {
    int answer = 0;
    if(n % 2 != 0)
        return 0;
    arr[0] = 1;
    arr[2] = 3;
    
    for(int i = 4 ; i <= n ; i+=2){
        arr[i] = (arr[i-2] * 3);
        for(int j = 0 ; j <= i-4 ; j += 2){
            arr[i] += (arr[j] * 2) % MOD;
        }
        arr[i] %= MOD;
    }
    
    
    
    answer = arr[n] % MOD;
    
    return answer;
}
//출처: https://bbeomgeun.tistory.com/71 [꾸준하게 차근차근:티스토리]