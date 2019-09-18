#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ll i,j,k,n,m,t;
    cin>>t;
    while(t--){
        cin>>n;
        ll a[n][n];
        string s;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++){
                cin>>s;
                if(s=="INF"){
                    a[i][j]=INT_MAX;
                } else {
                    k=stoi(s);
                    a[i][j]=k;
                }
            }
        
        for(k=0;k<n;k++){
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    a[i][j]=min(a[i][j],a[i][k]+a[k][j]);
                }
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(a[i][j]>=10000000)
                    cout<<"INF"<<" ";
                else
                    cout<<a[i][j]<<" ";
            }
            cout<<endl;
        }
    }
	return 0;
}
