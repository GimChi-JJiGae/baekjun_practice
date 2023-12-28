using namespace std;

int gcd(int a, int b){
    if (b == 0) return a;
    return gcd(b, a % b );
}

long long solution(int w,int h) {
    long long answer = 1;
    
    int gcd_num = gcd(w, h);    // 최대공약수, 즉 부분의 갯수
    int gcd_w = w / gcd_num;
    int gcd_h = h / gcd_num;
    
    long long total = (long long)w * (long long)h;
    
    answer = total - (gcd_w + gcd_h - 1) * gcd_num;
    
    return answer;
}