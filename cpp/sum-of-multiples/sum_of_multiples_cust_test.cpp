#include<boost/next_prior.hpp>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include"sum_of_multiples.h"

template<typename Iter, typename Cont>
bool is_last(Iter iter, const Cont& cont) {
  return (iter != cont.end() && (boost::next(iter) == cont.end()));
}

std::string to_string(std::vector<int> vec) {
  std::stringstream ss;
  for (std::vector<int>::iterator it=vec.begin(); it != vec.end(); ++it) {
    if (is_last(it, vec)) ss << *it;
    else ss << *it << ", ";
  }
  return ss.str();
}

int main() {
  using namespace sum_of_multiples;
  
  int ubnd = 100;
  intlist nums = {3, 5};
  intlist mults = bounded_multiples_of(nums, ubnd);

  std::cout << to_string(mults) << std::endl;

  std::cout << sum(mults) << std::endl;

  return 0;
}
