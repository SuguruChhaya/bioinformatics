#include <bits/stdc++.h>
using namespace std;

int main(){
    long long t, k;
    cin >> t >> k;
    vector<string> arr(t);
    for (long long i=0;i<t;i++){
        cin >> arr[i];
    }
    map<char, vector<long long>> d;
    vector<long long> temp (k, 0);
    set <char> chars = {'A', 'C', 'G', 'T'};
    for (auto e:chars){
        d[e] = temp;
    }   
    for (long long col = 0;col<k;col++){
        for (long long row = 0;row<t;row++){
            
        }
    }
}