#ifndef DIFFERENCE_OF_SQUARES_H
#define DIFFERENCE_OF_SQUARES_H

#include<functional>

namespace squares {
	int sum(int,std::function<int(int)>);
	int square(int);
	int square_of_sums(int);
	int sum_of_squares(int);
	int difference(int);
}

int squares::sum(int N, std::function<int(int)> f) {
	int result{0};
	for (int ii=1; ii <= N; ii++) result += f(ii);
	return result;
}

int squares::square(int i) { return i*i; }

int squares::square_of_sums(int N) {
	return squares::square(squares::sum(N, [](int i){ return i; }));
}

int squares::sum_of_squares(int N) {
	return squares::sum(N, squares::square);
}

int squares::difference(int N) { 
	return squares::square_of_sums(N) - squares::sum_of_squares(N);
}

#endif
