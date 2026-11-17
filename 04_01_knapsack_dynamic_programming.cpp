#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int n,W;cout<<"Number of items: ";cin>>n;cout<<"Capacity: ";cin>>W;
    vector<int> wt(n),val(n);
    for(int i=0;i<n;i++){cout<<"Weight and value of item "<<i+1<<": ";cin>>wt[i]>>val[i];}
    vector<vector<int>> dp(n+1,vector<int>(W+1,0));
    for(int i=1;i<=n;i++) for(int w=0;w<=W;w++){
        dp[i][w]=dp[i-1][w];
        if(wt[i-1]<=w) dp[i][w]=max(dp[i][w],val[i-1]+dp[i-1][w-wt[i-1]]);
    }
    cout<<"Maximum value = "<<dp[n][W]<<'\n';
    cout<<"Selected item numbers: ";int w=W;
    for(int i=n;i>0;i--) if(dp[i][w]!=dp[i-1][w]){cout<<i<<" ";w-=wt[i-1];}
    cout<<'\n';
}
