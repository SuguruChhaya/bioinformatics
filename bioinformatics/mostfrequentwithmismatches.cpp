#include <bits/stdc++.h>
using namespace std;
//*I guess kinda getting hard: http://rosalind.info/problems/ba1i/
//http://rosalind.info/search/?q=frequent+words
long long HammingDistance(string s1, string s2){
    long long ans = 0;
    for (long long i=0;i<s1.size();i++){
        if (s1[i]!=s2[i]){
            ans++;
        }
    }
    return ans;
}
map<string, long long> hash_map;
vector <char> chars = {'A', 'C', 'G', 'T'};
//!Time complexity is ass
void gen(long long k, long long start, long long currIndex, long long numWrong, string currString, string s, long long d){
    
    if (currString.size()==k){
        if (numWrong <= d){
            hash_map[currString]++;
        }
    }
    //If number of wrong exceeds then it just keeps running. 
    else{
        //*Different options. 
        for (auto e:chars){
            string nextString = currString;
            if (e==s[currIndex]){
                nextString.push_back(e);
                gen(k, start, currIndex+1, numWrong, nextString, s, d);
            }
            else{
                nextString.push_back(e);
                gen(k, start, currIndex+1, numWrong+1, nextString, s, d);
            }
        }
    }
}
//!I never found the motif matrix for t choices...
void count(string s, long long k, long long d){
    
    //*Keeps track of how many can show up. 
    for (long long i=0;i<=s.size()-k;i++){
        //*Generate all possible variations with at max d differences using recursion. 
        //*Information to store: starting index, current processing index, the number of mismatches
        gen(k, i, i, 0, "", s, d);
    }
    //*Count the element with the largest. 
    long long maxi = 0;
    for (auto p:hash_map){
        maxi = max(maxi, p.second);
    }
    for (auto p:hash_map){
        if (p.second==maxi){
            cout << p.first << " ";
        }
    }
    cout << endl;
}
int main(){
    string s;
    long long k, d;
    cin >> s >> k >> d;
    count(s, k ,d);
}