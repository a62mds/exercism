#ifndef LEAP_H
#define LEAP_H

bool Divides(int divisor, int dividend) {
	return dividend % divisor == 0;
}

namespace leap {
	bool is_leap_year(int input) {
		return Divides(4, input) && Divides(400, input)
			  || Divides(4, input) && !Divides(100, input);
	}
}

#endif
