#include <iostream>
#include <algorithm>
#include <vector>

int a[1000000], b[1000000];
using namespace std;
/*
a배열 b배열 받기.
두개의 변수로 각 요소 비교해주며 벡터에 넣어주기.
넣어줄 때 위치 가리키는 변수 움직여주기.
*/
int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	int N, M;
	int n = 0, m = 0;
	vector<int> v;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < M; i++) {
		cin >> b[i];
	}

	while (n < N && m < M) {
		if (a[n] < b[m]) {
			v.push_back(a[n++]);
		}
		else {
			v.push_back(b[m++]);
		}
	}
	while (n < N) {
		v.push_back(a[n++]);
	}
	while (m < M) {
		v.push_back(b[m++]);
	}

	for (int i = 0; i < M + N; i++) {
		cout << v[i] << " ";
	}

	return 0;
}