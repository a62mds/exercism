#include "prime_factors.h"

namespace prime_factors {
    std::vector<int> of(unsigned the_number) {
        std::vector<int> prime_factors;
        if (the_number >= 2) {
            unsigned divisor = 2;
            while (divisor * divisor <= the_number) {
                if (the_number % divisor == 0) {
                    prime_factors.push_back(divisor);
                    the_number /= divisor;
                } else {
                    divisor++;
                }
            }
            if (the_number > 1) {
                prime_factors.push_back(the_number);
            }
        }
        return prime_factors;
    }
}  // namespace prime_factors
