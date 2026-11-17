#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;
struct Item{double value,weight,ratio;int id;};
int bestValue=0; vector<int> bestSet;
void solve(const vector<Item>& a,int i,double weight,int value,double cap,vector<int>& chosen){
    if(weight>cap)return;
    if(i==(int)a.size()){if(value>bestValue){bestValue=value;bestSet=chosen;}return;}
    double bound=value, rem=cap-weight;
    for(int j=i;j<(int)a.size()&&rem>0;j++){double take=min(rem,a[j].weight);bound+=take*a[j].ratio;rem-=take;}
    if(bound<=bestValue)return;
    chosen.push_back(a[i].id);solve(a,i+1,weight+a[i].weight,value+(int)a[i].value,cap,chosen);chosen.pop_back();
    solve(a,i+1,weight,value,cap,chosen);
}
int main(){
    int n;double cap;cout<<"Number of items: ";cin>>n;cout<<"Capacity: ";cin>>cap;
    vector<Item>a(n);for(int i=0;i<n;i++){cout<<"Value and weight: ";cin>>a[i].value>>a[i].weight;
        if(a[i].weight<=0){cout<<"Weight must be positive.\n";return 1;}a[i].ratio=a[i].value/a[i].weight;a[i].id=i+1;}
    sort(a.begin(),a.end(),[](auto&x,auto&y){return x.ratio>y.ratio;});
    vector<int> chosen;solve(a,0,0,0,cap,chosen);
    cout<<"Maximum value = "<<bestValue<<"\nSelected item numbers: ";for(int x:bestSet)cout<<x<<" ";cout<<'\n';
}
