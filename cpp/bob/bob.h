#ifndef BOB_H
#define BOB_H

#include<algorithm>
#include<boost/algorithm/string.hpp>
#include<string>

bool is_question(std::string);
bool is_yelled(std::string);
bool is_empty(std::string);

namespace bob {

	std::string question_response{"Sure."};
	std::string yell_response{"Whoa, chill out!"};
	std::string empty_response{"Fine. Be that way!"};
	std::string default_response{"Whatever."};

	// Bob's hey function which returns a response based on the structure of the
	// string passed as input.
	std::string hey(std::string input) {
		boost::trim(input);	// trim leading and trailing whitespace
		if      ( is_question(input) ) { return bob::question_response; }
		else if ( is_yelled(input)   ) { return bob::yell_response;     }
		else if ( is_empty(input)    ) { return bob::empty_response;    }
		else                           { return bob::default_response;  }
	}

}

//
// Questions
bool is_question(std::string input) {
	// Question criteria: 
	// 	1) Last char is ?
	// 	2) Not yelled
	return input.back()=='?' && !is_yelled(input);
}

//
// Yelling
bool is_yelled(std::string input) {
	// Yelled criteria:
	// 	1) No lowercase letters
	// 	2) At least one alphabetic character
	return std::none_of(input.begin(), input.end(), ::islower)
			&& std::any_of(input.begin(), input.end(), ::isalpha);
}

//
// Whitespace
bool is_empty(std::string input) { 
	// Leading and trailing whitespace is trimmed in bob::hey(), so a string
	// consisting of all whitespace will be empty by the time it is passed here
	// as an argument.
	return input == "";
}

#endif
