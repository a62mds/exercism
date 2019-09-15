#include "binary.h"

#include<algorithm>
#include<cmath>

namespace binary {
    unsigned convert(std::string binary_number) {
        std::reverse(binary_number.begin(), binary_number.end());
        unsigned decimal_number = 0;
        for (unsigned idx=0; idx != binary_number.length(); ++idx) {
            char& digit = binary_number[idx];
            if (digit == '0') {
                continue;
            } else if (digit == '1') {
                decimal_number += std::pow(2, idx);
            } else {
                decimal_number = 0;
                break;
            }
        }
        return decimal_number;
    }
}  // namespace binary
