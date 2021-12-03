#include <bits/stdc++.h>
using namespace std;
map <string, long long>h;

long long HammingDistance(string s1, string s2){
    long long ans = 0;
    for (long long i=0;i<s1.size();i++){
        if (s1[i]!=s2[i]){
            ans++;
        }
        
    }
    return ans;
}
int main(){
    string s;
    long long k, d;
    cin >> s >> k >> d;
    vector <char> chars = {'A','T','C','G'};
    //*Generate all possible:
    deque <string> q;
    q.push_back("");
    while (!q.empty()){
        auto curr = q[0];
        if (curr.size()==k){
            h[curr] = 0;
        }
        else{
            for (auto c:chars){
                string next = curr;
                next.push_back(c);
                q.push_back(next);
            }
        }
    }
    for (long long i=0;i<=s.size();i++){
        for (auto p:h){
            if (HammingDistance(p.first, s.substr(i, k))){
                h[p.first]++;
            }
        }
    }
    long long maxi = 0;
    for (auto p:h){
        maxi = max(maxi, p.second);
    }
    for (auto p:h){
        if (p.second==maxi){
            cout << p.first << " ";
        }
    }
    cout << endl;
}