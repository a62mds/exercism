#include "hexadecimal.h"

#include<algorithm>
#include<cctype>
#include<cmath>

namespace hexadecimal {
    int char_to_uint(const char& hexadecimal_char) {
        switch (hexadecimal_char) {
            case '0': return 0;
            case '1': return 1;
            case '2': return 2;
            case '3': return 3;
            case '4': return 4;
            case '5': return 5;
            case '6': return 6;
            case '7': return 7;
            case '8': return 8;
            case '9': return 9;
            case 'a': return 10;
            case 'b': return 11;
            case 'c': return 12;
            case 'd': return 13;
            case 'e': return 14;
            case 'f': return 15;
            default:  return -1;
        }
    }
    unsigned convert(std::string hexadecimal_number) {
        std::reverse(hexadecimal_number.begin(), hexadecimal_number.end());
        unsigned decimal_number = 0;
        int value = 0;
        for (unsigned idx=0; idx < hexadecimal_number.length(); idx++) {
            value = char_to_uint(std::tolower(hexadecimal_number[idx]));
            if (value > 0) {
                decimal_number += value * std::pow(16, idx);
            } else if (value < 0) {
                decimal_number = 0;
                break;
            }
        }
        return decimal_number;
    }
}  // namespace hexadecimal
