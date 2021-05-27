vector<long long> matrixQueries(int n,int m,vector<vector<int>>  queries){
    set<int> sn;
    set<int>  sm;
    int i = 1;
    vector<long long> ve;
      while(i<=n){
          sn.insert(i);
      i++}
      i = 1;
     while(i<=m){
         sm.insert(i);
     i++;}
       
      for(auto p:queries){
          if(p.size()==1){
              ve.push_back((sn.begin())(*sm.begin()));
              continue;
          }
          if(p[0]==2){
              sm.erase(p[1]);
          }
          else if(p[0]==1){
              sn.erase(p[1]);
          }
      }
    return ve;
}