#include <fstream>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main() 
{
/*
  int size = 15;
  int a[] = {1, 
             2, 3, 
             4, 5, 6, 
             7, 8, 9, 10,
             11, 12, 13, 14, 15};
 */

  ifstream ifs("data.txt"); // input filestream
  if(!ifs)
    return 1;
  int sz=0;
  ifs >> sz;

  int row = 0;
  vector<vector<int>> vct;
  for (int i=0; i < sz; i += row )
  {
    row++;
    vector<int> vctofrow;
    for(int l = 0 ; l < row ; ++l)
    {
      int val;
      ifs >> val;
      vctofrow.push_back(val);
    }
    vct.push_back(vctofrow);
  }

  for (int k = vct.size()-1; k > 0 ; --k)
  {
    int above_row = k;
    int cur_row = k-1;  
    for(int l = 0 ; l < vct[cur_row].size(); ++l)
    {
      vct[cur_row][l] += std::max(vct[above_row][l], vct[above_row][l+1]);
    }
  }

  for(auto it = vct.begin(); it != vct.end(); ++it)
  {
    for(auto it2 = it->begin(); it2 != it->end(); ++it2  )    
      cout << *it2 << ' ';
    cout << endl;
  }

  cout << vct[0][0];
  return 0;
}
