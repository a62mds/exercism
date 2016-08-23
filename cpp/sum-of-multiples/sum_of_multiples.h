#ifndef SUM_OF_MULTIPLES_H
#define SUM_OF_MULITPLES_H

#include<algorithm>   // For std::max_element
#include<numeric>     // For std::accumulate
#include<vector>

namespace sum_of_multiples {

  // Fwd declarations
  int sum(std::vector<int>);
  std::vector<int> bounded_multiples_of(std::vector<int>, int);

  // Computes the sum of all multiples of the integers in nums less than ubnd
  int to(std::vector<int> nums, int ubnd) {
    if (ubnd <= *std::min_element(nums.begin(), nums.end()))
      return 0;
    else
      return sum(bounded_multiples_of(nums, ubnd));
  }

  // Computes the sum of all elements of in a vector of ints
  int sum(std::vector<int> nums) {
    int SUM_ID{0};
    return std::accumulate(nums.begin(), nums.end(), SUM_ID);
  }

  // Creates a vector of all multiples of the integers in nums that are less
  // than or equal to ubnd
  std::vector<int> bounded_multiples_of(std::vector<int> nums, int ubnd) {
    std::vector<int> multiples;
    for (std::vector<int>::iterator it=nums.begin(); it!=nums.end(); ++it)
      for (int ii=1; (*it)*ii < ubnd; ++ii) multiples.push_back((*it)*ii);
    return multiples;
  }

}

#endif
