#ifndef SUM_OF_MULTIPLES_H
#define SUM_OF_MULITPLES_H

#include<algorithm>   // For std::max_element
#include<numeric>     // For std::accumulate
#include<vector>

namespace sum_of_multiples {

  using intlist = std::vector<int>;

  //===
  // Helpers
  //---
  // Returns the sum of the integers in the intlist ns
  int sum(intlist ns) {
    return std::accumulate(ns.begin(), ns.end(), 0);
  }
  // Tests whether or not the intlist ns contains the int n
  bool contains(intlist ns, int n) {
    return (!ns.empty() && std::find(ns.begin(), ns.end(), n) != ns.end());
  }
  // Returns an intlist of all multiples of the integers in the intlist ns
  // that are strictly less than the upper bound ub
  intlist bounded_multiples_of(intlist ns, int ub) {
    intlist multiples;
    for (intlist::iterator it=ns.begin(); it!=ns.end(); ++it)
      for (int ii=1; (*it)*ii < ub; ii++) {
        int mult{(*it) * ii};
        if (!contains(multiples, mult)) multiples.push_back(mult);
      }
    return multiples;
  }

  //===
  // Primary
  //---
  // Computes the sum of all multiples of the integers in nums less than ubnd
  int to(intlist ns, int ub) {
    // Return 0 if nums is empty or if ubnd is less than all items in nums
    if (ns.empty() || (ub <= *std::min_element(ns.begin(), ns.end())))
      return 0;
    else 
      return sum(bounded_multiples_of(ns, ub));
  }

}

#endif
