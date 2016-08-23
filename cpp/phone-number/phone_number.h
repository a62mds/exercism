#ifndef PHONE_NUMBER_H
#define PHONE_NUMBER_H

#include<algorithm>
#include<cctype>
#include<string>

class phone_number {
	public:
    // Default constructor
		phone_number(std::string raw_num=INVALID_NUM) 
			: m_num(filter_valid(filter_digits(raw_num)))
    {}

    // Member variable m_num getter
		std::string number() const { return m_num; }

    // Area code getter
		std::string area_code() const { return m_num.substr(0,3); }

    // Casts a phone_number object into an std::string
		operator std::string() const { return format(m_num); }

	private:
    // Constant number of digits in valid phone number
    static const int VALID_LENGTH;

    // Constant assigned to m_num when invalid phone number is passed as input
    static const std::string INVALID_NUM;

    // Member variable holding filtered (digits only) and verified phone number
		std::string m_num;

    // Removes all non-digits from a string
		std::string filter_digits(std::string);

    // Ensures correct number of digits, else returns INVALID_NUM
		std::string filter_valid(std::string);

    // Formats phone number for casting as std::string
		std::string format(std::string) const;
};

//============================================================================
// Constants:
const int phone_number::VALID_LENGTH = 10;
const std::string phone_number::INVALID_NUM = "0000000000";

//============================================================================
// Methods:

//===
// Removes all non-digits from a string
// -> std::remove_if(first, last, pred) removes all elements satisfying the
//    specific criteria defined via pred from the specified range [last, first)
//     -> NOTE: it does not change the physical size of the container, it simply
//        re-orders the container so that elements satisfying the criteria are
//        shifted to the beginning, maintaining their relative order
//     -> the elements removed are shifted to the end of the list and are 
//        dereferenceable, but have unspecified values
//     -> then returns an iterator pointing just beyond the last unremoved item
// -> std::string.erase(start, end) removes these unspecified values, reducing
//    the physical size of the string to match its new logical size, by trimming
//    the string from the iterator <start> returned by remove_if to the end of
//    the original string at <end>
std::string phone_number::filter_digits(std::string num) {
  using std::remove_if;
  using std::isdigit;
  num.erase(
    remove_if(num.begin(), num.end(), [](char c) { return !isdigit(c); }),
    num.end()
  );
  return num;
}

//===
// Ensures correct number of digits, else returns INVALID_NUM
std::string phone_number::filter_valid(std::string ph_num) {
	if (ph_num.length() == VALID_LENGTH)
    return ph_num;
  else if ( (ph_num.length() == VALID_LENGTH+1) && (ph_num[0] == '1') )
    return ph_num.erase(0,1);
	else
    return INVALID_NUM;
}

//===
// Formats m_num for casting as std::string
std::string phone_number::format(std::string ph_num) const {
	return "("+ph_num.substr(0,3)+") "+ph_num.substr(3,3)+"-"+ph_num.substr(6,4);
}

#endif
