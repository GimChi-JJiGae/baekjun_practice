
#include <iostream>
#include <algorithm>
#include <vector>

//using namespace std;
//
//int main()
//{
//    int L, C;
//    cin >> L >> C;
//
//    vector<char> jaeum;
//    vector<char> moeum;
//
//    char vowels[] = { 'a', 'e', 'i', 'o', 'u' };
//
//    char *p = find(vowels, vowels + 5, 'b');
//    
//    for (int i = 0; i < L; i++) {
//        if (p == vowels + 5) {                  // 자음
//            cout << "여기" << endl;
//        }
//        else {                                  // 모음
//            cout << *p;
//        }
//    }
//    
//    
//
//    return 0;
//
//}

using namespace std;
typedef long long int ll;
int L, C;
vector<char> v;
vector<char> res;

bool check()
{
    int moum = 0;
    for (int i = 0; i < L; i++)
    {
        if (res[i] == 'a' ||
            res[i] == 'e' ||
            res[i] == 'i' ||
            res[i] == 'o' ||
            res[i] == 'u')
            moum++;
    }
    // 모음의 수 1개 이상, 자음의수 = 전체수 -모음의 수 . 2개이상.
    if (moum >= 1 && L - moum >= 2) return true;
    return false;
}
void dfs(int d) {
    if ((int)res.size() == L) {
        if (check()) { //check에서 조건 부합시 출력.
            for (int k = 0; k < L; k++)
            {
                cout << res[k];
            }
            cout << '\n';
        }
        return;
    }
    for (int i = d; i < C; i++)
    {
        res.push_back(v[i]); //들어갈때 하나씩 추가해주고
        dfs(i + 1);
        res.pop_back(); //나오면 하나 빼주고.
    }
    return;
}
int main(void)
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> L >> C;
    for (int i = 0; i < C; i++)
    {
        char temp;
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end()); //정렬하고 dfs(0)시작.
    dfs(0);
}