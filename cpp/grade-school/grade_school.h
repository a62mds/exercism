#ifndef GRADE_SCHOOL_H
#define GRADE_SCHOOL_H

#include<algorithm>
#include<stdexcept>
#include<map>
#include<string>
#include<vector>

using name_t = std::string;
using grade_t = int;
using namelst_t = std::vector<name_t>;
using roster_t = std::map<grade_t,namelst_t>;

using namelstit_t = namelst_t::iterator;
using rosterit_t = roster_t::iterator;

namespace grade_school {
	class school {
		public:
			roster_t m_roster;
			roster_t roster() const { return m_roster; }
			namelst_t grade(grade_t gr_no) const;
			void add(name_t,grade_t);
		private:
			void sort_names(namelst_t&);
	};
}

namelst_t grade_school::school::grade(grade_t grade_no) const {
	try {
		return m_roster.at(grade_no);
	} catch (std::out_of_range) {
		namelst_t empty;
		return empty;
	}
}

void grade_school::school::add(name_t name, grade_t gr_no) {
	m_roster[gr_no].push_back(name);
	sort_names(m_roster[gr_no]);
}

void grade_school::school::sort_names(namelst_t& names) {
	std::sort(names.begin(),names.end());
}

#endif
