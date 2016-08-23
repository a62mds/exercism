#ifndef NUCLEOTIDE_COUNT_H
#define NUCLEOTIDE_COUNT_H

#include<stdexcept>
#include<map>
#include<string>

namespace dna {
	class counter {
		public:
			std::string m_seq;
			std::map<char,int> m_count;
			counter(std::string seq) : m_seq(seq), m_count(seq_count(seq)) {}
			std::map<char,int> nucleotide_counts() const { return m_count; }
			int count(char) const;
		private:
			std::map<char,int> seq_count(std::string&);
			bool is_in(char,std::string) const;
	};
}

std::map<char,int> dna::counter::seq_count(std::string& seq) {
	std::map<char,int> count{{'A',0},{'T',0},{'C',0},{'G',0}};
	for (std::string::iterator it=seq.begin(); it!=seq.end(); ++it) {
		switch (*it) {
			case 'A': count['A']++; break;
			case 'T': count['T']++; break;
			case 'C': count['C']++; break;
			case 'G': count['G']++; break;
			default: throw std::invalid_argument(*it+" is invalid");
		}
	}
	return count;
}

int dna::counter::count(char nuc) const {
	if (!is_in(nuc,"ATCG")) 
		throw std::invalid_argument(nuc+" is invalid");
	return m_count.at(nuc);
}

bool dna::counter::is_in(char nuc, std::string seq) const {
	return seq.find(nuc) != std::string::npos;
}

#endif
