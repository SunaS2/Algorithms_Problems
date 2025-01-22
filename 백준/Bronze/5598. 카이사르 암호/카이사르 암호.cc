#include <iostream>
#include <string>
using namespace std;

int main() {
	 
	string S;
	cin >> S;


	for (int i = 0; i < S.size();i++) {
		S[i] -= 3;

		if (S[i] < 'A') {
			S[i] += 26;
		}
	}

	cout << S;
	

	return 0;
}