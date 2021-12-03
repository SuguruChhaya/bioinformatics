#include <bits/stdc++.h>
using namespace std;
//http://rosalind.info/problems/ba2c/

double pr(string s, map<char, vector <double>>d){
    double ans = 1;
    for (long long i=0;i<s.size();i++){
        ans *= d[s[i]][i];
    }
    return ans;
}

void solve(){
    string s;
    long long k;
    cin >> s >> k;
    //*k mer doesn't have to be the most FRQUENT k mer. 
    //*Just have to be a substring. 
    map <char, vector <double>> d;
    vector <char> chars = {'A', 'C', 'G', 'T'};
    //*The idea is that it is stored in a map. 
    for (long long i=0;i<4;i++){
        for (long long j=0;j<k;j++){
            double temp;
            cin >> temp;
            d[chars[i]].push_back(temp);
        }
    }
    double maxi = 0;
    for (long long i=0;i<=s.size()-k;i++){
        maxi = max(maxi, pr(s.substr(i, k), d));
    }
    for (long long i=0;i<=s.size()-k;i++){
        if (pr(s.substr(i, k), d)==maxi){
            cout << s.substr(i, k) << endl;
            return;
        }
    }
}

int main(){
    solve();
    return 0;
    string s;
    long long k;
    cin >> s >> k;
    
    map <char, vector <double>> d;
    vector <char> chars = {'A', 'C', 'G', 'T'};
    //*The idea is that it is stored in a map. 
    for (long long i=0;i<4;i++){
        for (long long j=0;j<k;j++){
            double temp;
            cin >> temp;
            d[chars[i]].push_back(temp);
        }
    }
    /*
    for (auto p:d){
        cout << p.first << endl;
        for (auto e:p.second){
            cout << e << endl;
        }
    }
    */
    //*Find the k mer. 
    map <string, long long> h;
    for (long long i=0;i<=s.size()-k;i++){
        h[s.substr(i, k)]++;
    }
    /*
    for (auto p:h){
        cout << p.first << " " << p.second << endl;
    }
    */
    long long maxi = 0;
    for (auto p:h){
        if (p.second>maxi){
            maxi = p.second;
        }
    }
    vector <string> kmers;
    /*
    for (auto p:h){
        if (p.second==maxi){
            kmers.push_back(p.first);
        }
    }
    */
    //!Don't want to loop through the k mers in the wrong order. 
    //*Loop through the beginning and check whether we have added that kmer yet. 
    for (long long i=0;i<s.size()-k;i++){
        if (h.count(s.substr(i, k)) && h[s.substr(i, k)]==maxi){
            kmers.push_back(s.substr(i, k));
        }
    }
    double maxi2 =0;
    vector <string> ans;
    for (auto e:kmers){
        if (e=="TGTCGC"){
            cout << "";
        }
        if (pr(e, d)>maxi2){
            maxi2 = pr(e, d);
        }
    }
    for (auto e:kmers){
        if (pr(e,d)==maxi2){
            ans.push_back(e);
        }
    }
    cout << ans[0] << endl;
    
}