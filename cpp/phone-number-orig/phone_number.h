#ifndef PHONE_NUMBER_H
#define PHONE_NUMBER_H

#include<algorithm>
#include<cctype>
#include<string>

class phone_number {
	public:
		phone_number(std::string ph_num) 
			: m_number(verify_valid_length(strip_punct(ph_num))) {}
		std::string number() const { return m_number; }
		std::string area_code() const { return m_number.substr(0,3); }
		operator std::string() const { return fmt_ph_num(m_number); }
	private:
		std::string m_number{""};
		std::string strip_punct(std::string);
		std::string verify_valid_length(std::string);
		std::string fmt_ph_num(std::string) const;
};

std::string phone_number::strip_punct(std::string num) {
  using std::remove_if;
  using std::isdigit
	return num.erase(
    remove_if(num.begin(), num.end(), [](char c){ return !isdigit(c); }),
    num.end()
  );
}

std::string phone_number::verify_valid_length(std::string ph_num) {
	if      (ph_num.length()==10                  ) { return ph_num;            }
	else if (ph_num.length()==11 && ph_num[0]=='1') { return ph_num.erase(0,1); }
	else                                            { return "0000000000";      }
}

std::string phone_number::fmt_ph_num(std::string ph_num) const {
	return "("+ph_num.substr(0,3)+") "+ph_num.substr(3,3)+"-"+ph_num.substr(6,4);
}

#endif
