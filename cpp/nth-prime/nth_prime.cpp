#include "nth_prime.h"
#include <stdexcept>

unsigned nth_prime::nth(unsigned n) {
    if (n <= 0) {
        throw std::domain_error("Bad argument (<= 0)");
    }
    if (n == 1) {
        return 2;
    }
    unsigned num_primes_found = 1;
    unsigned dividend = 3;
    while (true) {
        if (is_prime(dividend)) {
            num_primes_found++;
        }
        if (num_primes_found == n) {
            break;
        } else {
            dividend += 2;
        }
    }
    return dividend;
}

bool nth_prime::is_prime(unsigned n) {
    if (n < 2) {
        return false;
    } else if (n % 2 == 0) {
        return n == 2;
    }
    for (unsigned divisor=3; divisor <= (n - 1) / 2; divisor += 2) {
        if (n % divisor == 0) {
            return false;
        }
    }
    return true;
}
