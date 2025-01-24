#include <iostream>

using namespace std;

int main() {
	
	bool student[31] = {false};
	int idx = 0;

	for (int i = 0; i < 28;i++) {
		cin >> idx;
		student[idx] = true;
	}

	for (int j = 1;j <= 30;j++) {
		if (student[j] == false) {
			cout << j <<'\n';
		}
	}
	
	return 0;
}