#include <iostream>
#include <vector>
using namespace std;
int n, solutions=0;
bool safe(const vector<int>& q,int row,int col){
    for(int r=0;r<row;r++) if(q[r]==col || abs(q[r]-col)==abs(r-row)) return false;
    return true;
}
void place(vector<int>&q,int row){
    if(row==n){solutions++;cout<<"Solution "<<solutions<<":\n";
        for(int r=0;r<n;r++){for(int c=0;c<n;c++)cout<<(q[r]==c?"Q ":" . ");cout<<'\n';}cout<<'\n';return;}
    for(int c=0;c<n;c++)if(safe(q,row,c)){q[row]=c;place(q,row+1);}
}
int main(){cout<<"Enter N (1 to 15): ";cin>>n;if(n<1||n>15){cout<<"Invalid N.\n";return 1;}
    vector<int>q(n,-1);place(q,0);cout<<"Total solutions = "<<solutions<<'\n';}
