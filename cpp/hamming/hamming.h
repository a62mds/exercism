#ifndef HAMMING_H
#define HAMMING_H

#include<stdexcept>
#include<string>

namespace hamming {
	int compute(std::string str1, std::string str2) {
		// std::domain_error used to report situations where the inputs are outside
		// of the domain on which compute is defined. Since the Hamming distance is
		// defined only when sequences are the same length, the inputs are outside
		// of compute's domain when they are of unequal length.
		if (str1.length() != str2.length())
			throw std::domain_error("Sequences must have equal length");

		// Compare sequences letter by letter and add 1 to the Hamming distance if
		// they do not match.
		int dist{0};
		for (int ii=0; ii < str1.length(); ii++) {
			if (str1[ii] != str2[ii]) dist++;
		}

		return dist;
	}
}

#endif
