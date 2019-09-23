#include "reverse_string.h"

#include<algorithm>

namespace reverse_string {
    std::string reverse_string(std::string the_string) {
        std::reverse(the_string.begin(), the_string.end());
        return the_string;
    }
}  // namespace reverse_string
