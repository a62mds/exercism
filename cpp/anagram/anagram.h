#ifndef ANAGRAM_H
#define ANAGRAM_H

#include<boost/algorithm/string.hpp>
#include<map>
#include<string>
#include<vector>

using wordIt = std::string::iterator;
using wordList = std::vector<std::string>;
using wordListIt = std::vector<std::string>::iterator;

namespace anagram {
	class anagram {
		private:
			std::string m_lc_word;

		public:
			std::string m_word;

			anagram(std::string word="") : m_word(word), m_lc_word(word) {
				boost::algorithm::to_lower(m_lc_word);
			}

			wordList matches(wordList);
	};

	bool is_permutation(std::string, std::string);
	std::map<char,int> count_letters(std::string);
}

wordList anagram::anagram::matches(wordList words) {
	std::vector<std::string> output;

	for (wordListIt it=words.begin(); it!=words.end(); ++it) {
		std::string cpy{*it};
		boost::algorithm::to_lower(cpy);
		if      (m_lc_word == cpy)               { continue;              }
		else if (is_permutation(m_lc_word, cpy)) { output.push_back(*it); }
	}

	return output;
}

bool anagram::is_permutation(std::string word1, std::string word2) {
	return count_letters(word1) == count_letters(word2);
}

std::map<char,int> anagram::count_letters(std::string word) {
	std::map<char,int> letter_count;
	for (wordIt it=word.begin(); it != word.end(); ++it) letter_count[*it]++;
	return letter_count;
}

#endif
