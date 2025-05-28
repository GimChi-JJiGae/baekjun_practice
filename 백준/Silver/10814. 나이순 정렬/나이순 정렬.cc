#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(){
    
    int N;
    int age;
    string name;
    cin >> N;
    
    map<int, vector<string>> people;
    
    for(int i = 0; i < N; i++){
        cin >> age >> name;
        people[age].push_back(name);
    }
    
    for (const auto& [age, names] : people){
        for (const auto& name : names){
            cout << age << " " << name << "\n";    
        }
    }
    
    return 0;
}