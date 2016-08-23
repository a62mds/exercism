#ifndef FOOD_CHAIN_H
#define FOOD_CHAIN_H

#include<string>
#include<utility>
#include<vector>

using verselist_t = std::vector<std::pair<std::string,std::string>>;

namespace food_chain {
	std::vector<std::string> up_list = {
		"I know an old lady who swallowed a fly.\n",
		"I know an old lady who swallowed a spider.\n"
			"It wriggled and jiggled and tickled inside her.\n",
		"I know an old lady who swallowed a bird.\n"
			"How absurd to swallow a bird!\n",
		"I know an old lady who swallowed a cat.\n"
			"Imagine that, to swallow a cat!\n",
		"I know an old lady who swallowed a dog.\n"
			"What a hog, to swallow a dog!\n",
		"I know an old lady who swallowed a goat.\n"
			"Just opened her throat and swallowed a goat!\n",
		"I know an old lady who swallowed a cow.\n"
			"I don't know how she swallowed a cow!\n",
		"I know an old lady who swallowed a horse.\n"
			"She's dead, of course!\n"
	};
	std::vector<std::string> pd_list = {
		"I don't know why she swallowed the fly. Perhaps she'll die.\n",
		"She swallowed the spider to catch the fly.\n",
		"She swallowed the bird to catch the spider that wriggled and jiggled and "
			"tickled inside her.\n",
		"She swallowed the cat to catch the bird.\n",
		"She swallowed the dog to catch the cat.\n",
		"She swallowed the goat to catch the dog.\n",
		"She swallowed the cow to catch the goat.\n"
	};
	std::string unique_part(int);
	std::string pass_down(int);
	std::string verse(int);
	std::string verses(int,int);
	std::string sing();
}

std::string food_chain::unique_part(int v_no) { return up_list[v_no]; }

std::string food_chain::pass_down(int v_no) {
	return v_no==0 ? pd_list[v_no] : pd_list[v_no]+pass_down(v_no-1);
}

std::string food_chain::verse(int v_no) {
	return v_no==8 ? unique_part(v_no-1) : unique_part(v_no-1)+pass_down(v_no-1);
}

std::string food_chain::verses(int v_start, int v_end) {
	std::string song_fragment{""};
	for (int ii=v_start; ii<=v_end; ii++) song_fragment+=verse(ii)+"\n";
	return song_fragment;
}

std::string food_chain::sing() { return verses(1,8); }

#endif
