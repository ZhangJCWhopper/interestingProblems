#include <iostream>
#include <string>
#include <vector>
#include<algorithm>

using namespace std;

#define M 2005
bool d[3][3][M];

int max(int a, int b){
    if (a > b) return a;
    return b;
}
int ans = M * 3;
void check(string a, string b, string c){
    vector <string> s;
    s.push_back(a);
    s.push_back(b);
    s.push_back(c);
    
    int i, j, k;
    // record all the matching true/false
    // str i and str j, pos k, match or not
    for (i=0;i<3;i++)
        for(j=0;j<3;j++)
            for(k=0;k<s[i].size();k++){
                if (i>= j) continue;
                bool ok = true;
                for (int ni =k; ni<s[i].size();ni++){
                    int nj = ni - k;
                    if (nj >= s[j].size()) break;
                    if (s[i][ni]=='?' || s[j][nj]=='?') continue;
                    if (s[i][ni] != s[j][nj]) ok = false;
                }
                d[i][j][k] = ok;
            }
    for (i=0;i<M;i++)
        for (j=0;j < M;j++){
            if (i < s[0].size() && !d[0][1][i]) continue;
            if (j < s[1].size() && !d[1][2][j]) continue;
            if (i+j < s[0].size() && !d[0][2][i+j]) continue;
            int now = 0;
            now = max(now, (int)s[0].size());
            now = max(now, i + (int)s[1].size());
            now = max(now, i + j + (int)s[2].size());
            ans = min(ans, now);
        }
}


int main()
{
    int i;
    vector<string> s(3);
    for (i=0;i<3;i++)
        cin >> s[i];
    
    sort(s.begin(), s.end());
    
    check(s[0], s[1], s[2]);
    check(s[0], s[2], s[1]);
    check(s[1], s[0], s[2]);
    check(s[1], s[2], s[0]);
    check(s[2], s[0], s[1]);
    check(s[2], s[1], s[0]);
    
    cout << ans<<endl;
    return 0;
}
