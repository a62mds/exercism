#include "sieve.h"

namespace sieve {

    class Number {
        public:
            enum NumType {
                prime,
                nonprime,
                unknown
            };
            Number(unsigned v, NumType t=unknown) :
                value(v),
                type(t)
            {}
            void set_type(NumType t) { type = t; }
            unsigned get_value() const { return value; }
            bool has_type(NumType t) const { return type == t; }
        private:
            unsigned value;
            NumType type;
    };

    std::vector<int> primes(unsigned upper_bound) {
        if (upper_bound < 2) {
            return std::vector<int>();
        }

        std::vector<Number> numbers;
        for (unsigned ii=0; ii <= upper_bound; ii++) {
            numbers.push_back(Number(ii));
        }
        numbers[0].set_type(Number::nonprime);
        numbers[1].set_type(Number::nonprime);

        unsigned factor;
        unsigned multiple;
        for (std::vector<Number>::iterator number=numbers.begin(); number != numbers.end(); ++number) {
            if (number->has_type(Number::nonprime)) {
                continue;
            }
            number->set_type(Number::prime);
            factor = 2;
            while (true) {
                multiple = number->get_value() * factor;
                if (multiple > upper_bound) {
                    break;
                }
                numbers[multiple].set_type(Number::nonprime);
                factor++;
            }
        }

        std::vector<int> the_primes;
        for (int ii=2; ii <= (int)upper_bound; ii++) {
            if (numbers[ii].has_type(Number::prime)) {
                the_primes.push_back(ii);
            }
        }

        return the_primes;
    }

}  // namespace sieve
