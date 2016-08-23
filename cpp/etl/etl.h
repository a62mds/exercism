#ifndef ETL_H
#define ETL_H

#include<cctype>
#include<map>
#include<vector>

using old_t = std::map<int,std::vector<char>>;
using new_t = std::map<char,int>;

using vit_t = std::vector<char>::iterator;
using oit_t = old_t::iterator;
using nit_t = new_t::iterator;

namespace etl {
	new_t transform(old_t);
}

new_t etl::transform(old_t old_score) {
	new_t new_score;
	for (oit_t oit=old_score.begin(); oit!=old_score.end(); ++oit)
		for (vit_t vit=(oit->second).begin(); vit!=(oit->second).end(); ++vit)
			new_score[std::tolower(*vit)] = oit->first;
	return new_score;
}

#endif
