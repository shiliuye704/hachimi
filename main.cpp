#include <iostream>
#include "mathfunc.h"
using namespace std;

int main() {
	int x , y ;
	cout << "请输入两个整数：" << endl;
	cin >> x >> y;
	cout << "两个数的和为：" << add(x, y) << endl;
	cout << "两个数的积为：" << multiply(x, y) << endl;
	return 0;
}
