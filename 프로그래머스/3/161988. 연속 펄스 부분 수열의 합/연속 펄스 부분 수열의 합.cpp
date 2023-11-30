#include <string>
#include <vector>
#include <iostream>

#define INF 987654321;

using namespace std;

long long max(long long a, long long b){
    if (a > b)
        return a;
    else return b;
}

long long solution(vector<int> sequence) {
    long long answer = 0;
    long long psum = 0;
    long long ret = -INF;
    vector<long long> arr;
    for(int i = 0 ; i< sequence.size() ; i++){
        arr.push_back(sequence[i]);
        if(i % 2 == 1)
            arr[i] *= -1;
    }
    for(int i = 0 ; i < arr.size(); i++){
        psum = max(psum,0) + arr[i];
        ret = max(ret, psum);
    }
    psum = 0;
    for(int i = 0 ; i < arr.size(); i++){
        psum = max(psum,0) - arr[i];
        ret = max(ret, psum);
    }
    
    return ret;
}