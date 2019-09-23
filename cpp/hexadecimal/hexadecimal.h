#if !defined(HEXADECIMAL_H)
#define HEXADECIMAL_H

#include<string>

namespace hexadecimal {
    int char_to_uint(const char& hexadecimal_char);
    unsigned convert(std::string hexadecimal_number);
}  // namespace hexadecimal

#endif // HEXADECIMAL_H