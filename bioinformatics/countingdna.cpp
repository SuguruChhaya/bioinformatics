#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    map <char, long long> d;
    for (auto e:s){
        d[e]++;
    }
    cout << d['A'] << " " << d['C'] << " " << d['G'] << " " << d['T'] << endl;     
}