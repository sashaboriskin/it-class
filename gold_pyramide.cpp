#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
//7 2 3 3 3 1 3 1 5 4 3 1 3 1 3 2 2 2 2 2 2 5 6 4 5 6 4 3


int prize(vector<int> n, int cur_el) {
    if (cur_el лежит на самом нижнем слое) // 5 6 4 5 6 4 3
        return n[cur_el];
    else
        return n[cur_el]+max из его потомков прямо под ним

}


int main()
{
    ifstream ifs("data.txt"); // input filestream
    vector<int> num;
    int buf=0;
    int sz=0;
    int n=0;
    ifs >> sz;

    for (int i=0; i<sz; i++) {
        ifs >> buf;
        num.push_back(buf);
    }

    for (int i=0; i<num.size(); i=i+(1+n)) {
        cout << n+1 << " " << num[i] << endl;
        n++;
    }

    
    
/*
    cout << num[0] << endl;
    cout << num[1] << endl;
    cout << num[3] << endl;
    cout << num[6] << endl;
    cout << num[10] << endl;
    cout << num[15] << endl;
*/


    return 0;
}
