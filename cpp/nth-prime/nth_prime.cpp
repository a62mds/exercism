#include "nth_prime.h"
#include <stdexcept>

namespace nth_prime {
    int nth(int n) {
        if (n <= 0) {
            throw std::domain_error("Bad argument (<= 0)");
        }
        int n_primes_found = 0;
        int dividend = 0;
        while (n_primes_found < n) {
            dividend++;
            if (is_prime(dividend)) {
                n_primes_found++;
            }
        }
        return dividend;
    }

    bool is_prime(int dividend) {
        if (dividend < 2) {
            return false;
        }
        else if (dividend == 2) {
            return true;
        }
        else if (dividend % 2 == 0) {
            return false;
        }

        for (int divisor=2; divisor <= (dividend - 1) / 2; divisor++) {
            if (dividend % divisor == 0) {
                return false;
            }
        }
        return true;
    }
}  // namespace nth_prime
