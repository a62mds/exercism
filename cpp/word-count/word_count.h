#ifndef WORD_COUNT_H
#define WORD_COUNT_H

#include<algorithm>
#include<boost/algorithm/string.hpp>
#include<cctype>
#include<map>
#include<string>
#include<vector>

using word_t = std::string;
using count_t = int;
using wordct_t = std::map<word_t,count_t>;
using wordlist_t = std::vector<word_t>;

using wit_t = word_t::iterator;
using wlit_t = wordlist_t::iterator;

namespace word_count {
	wordct_t words(std::string);
	void strip_punctuation(word_t&);
}

struct isPunctSp {
	bool operator()(char c) { return std::ispunct(c) && !c=='\''; }
};

wordct_t word_count::words(std::string phrase) {
	wordct_t count;
	wordlist_t words;
	boost::split(words,phrase,boost::is_any_of(" \t\n,"));
	for (wlit_t wlit=words.begin(); wlit!=words.end(); ++wlit) {
		word_count::strip_punctuation(*wlit);
		boost::algorithm::to_lower(*wlit);
		if ((*wlit).length() > 0) count[*wlit]++;
	}
	return count;
}

void word_count::strip_punctuation(word_t& word) {
	for (wit_t wit=word.end(); wit >= word.begin(); --wit) {
		if (std::ispunct(*wit)) { word.erase(wit); }
		else if (std::isalnum(*wit)) { break; }
	}
	for (wit_t wit=word.begin(); wit != word.end(); ++wit) {
		if (std::ispunct(*wit)) { word.erase(wit); }
		else if (std::isalnum(*wit)) { return; }
	}
}

#endif
