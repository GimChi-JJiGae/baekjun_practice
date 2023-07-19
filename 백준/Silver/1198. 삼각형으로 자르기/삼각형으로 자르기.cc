
#include <iostream>
#include <cmath>

using namespace std;

double calculateTriangleArea(int x1, int y1, int x2, int y2, int x3, int y3) {
    // 세 변의 길이 계산
    double a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    double b = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double c = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));

    // 반 둘레 계산
    double s = (a + b + c) / 2.0;

    // 넓이 계산
    double area = sqrt(s * (s - a) * (s - b) * (s - c));

    return area;
}

int main()
{
    double max_triangle = 0;

    int N;
    pair<int, int> p_arr[35];           // 페어 어레이 만들어두기
    cin >> N;
    for (int i = 0; i < N; i++) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        p_arr[i].first = tmp1;
        p_arr[i].second = tmp2;
    }

    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                double tmp_area = calculateTriangleArea(p_arr[i].first, p_arr[i].second, p_arr[j].first, p_arr[j].second, p_arr[k].first, p_arr[k].second);
                if (tmp_area > max_triangle) {
                    max_triangle = tmp_area;
                }
            }
        }
    }
    cout.precision(11); // 이게뭐지?
    cout << max_triangle;
}